# Stuff related to plotting, matplotlib, seaborn, etc.
import matplotlib.pyplot as plt
import matplotlib.patheffects as PathEffects
import numpy as np

common_rcParams = {
    'figure.figsize':(7.5,5)   , # (width,height, , convention: wide = 1.5*tall, size of canvas
    'figure.dpi':150   ,    # scales elements on canvas. Default 100 
    'axes.labelsize': 12 ,
    'axes.titlesize': 13 ,
    'axes.linewidth': 1.2 ,
    'grid.linestyle': '-.' ,
    'grid.alpha': 0.4 ,
    'lines.linewidth': 2  ,
    'legend.framealpha': 1.0  ,
    'legend.shadow': False  ,
    'font.size': 14 ,
    'xtick.labelsize': 12 ,
    'xtick.major.size': 8 , # default 3 
    'xtick.minor.size': 5 ,  
    'xtick.major.width': 1.2 , # default 0.8 
    'xtick.direction': 'inout' ,
    #'xtick.top': True ,
    'ytick.labelsize': 12 ,
    'ytick.major.size': 8 , # default 3 
    'ytick.minor.size': 5 , 
    'ytick.major.width': 1.2 , # default 0.8 
    'ytick.direction': 'inout'  ,
    'ytick.right': True ,
}

def make_better_plots():
    plt.rcParams.update( common_rcParams )

def writeLetterGrade(xpos,ypos,text,Qinfo,lettercolor='black',strokecolor='#bec1c1'):
    txt = plt.text(xpos,ypos,text,color=lettercolor,fontsize=Qinfo["lettergrade_fs"],va='center',ha='center')
    txt.set_path_effects([PathEffects.withStroke(linewidth=3, foreground=strokecolor)])
    return() 



# Common functions 

def gen_IntegerHisto(scores,maxScore,Qinfo,letters,title,bins,tick_list,cbar,outname=None):

    # stats shift 
    stat_shift = -0.08 


    # Data prep 
    maxScore = int(maxScore) 
    scores.sort()
    numScore = len(scores) 

    # Check 
    maxScore_dic = Qinfo["numPoints"]
    assert maxScore==maxScore_dic , f"Gradebook max score {maxScore} != your provided max score {maxScore_dic}"

    # Generate the histogram data (no plot yet)
    weights = (1/numScore)*np.ones(numScore) # makes sum(heights) = 1, individual height = fraction of class 
    bars, bins = np.histogram(scores,bins,weights=weights)
    #print(f'Sum of bar heights: {sum(bars)}')

    # Determine heights of letter grade bins 
    lgrade = list(letters.keys())
    lgrade.reverse() 
    lbins = list(letters.values())
    lbins.reverse() 
    lbins += [maxScore+1]
    lbars, lbins = np.histogram(scores,lbins,weights=weights)
    #print(f'Sum of letter grade bar heights: {sum(lbars)}')

    # Cumulative 
    # =-=-=-==-=-=-==-=-=-==-=-=-==-=-=-=

    # cumulative by bars 
    cumbars = np.zeros(len(bars))
    for i in range(len(bars)):
        cumbars[i] = sum(bars[0:(i+1)])

    # cumulative by individual scores 
    cumscores = np.arange(1,1+numScore,1)/numScore

    # colorbars (pass in numbers between 0 and 1 and they are mapped to colors)
    lcolorbar = cbar([x/(maxScore) for x in lbins])
    scolorbar = cbar([x/(bins[-1]) for x in bins])
    #print(lcolorbar,[x/(maxScore+1) for x in lbins])

    # Max bar for ylim adjustments 
    bar_max = max( max(lbars) , max(bars) )

    # Now make the histograms (bar allows you to pass a color array)
    plt.bar(lbins[:-1], lbars, width=np.diff(lbins), align='edge', color=lcolorbar, alpha=0.5, edgecolor='none',zorder=0) 
    #plt.bar(lbins[:-1], lbars, width=np.diff(lbins), align='edge', color='none', edgecolor='white', linewidth=4, zorder=1)
    plt.bar(bins[:-1], bars, width=np.diff(bins), align='edge', color=scolorbar, alpha=1, edgecolor='black', zorder=1) 

    plt.xlabel(Qinfo["xlabel"])
    plt.ylabel('Fraction of the Class')


    # Pad ylim, center xlim 
    ymax = Qinfo["ypadding_fac"]*bar_max
    if(len(tick_list[1])>0 and tick_list[1][-1]>ymax): # user tick marks all displayed 
        ymax = tick_list[1][-1]
    dy = ymax - 0 
    plt.ylim([0,ymax])
    
    dx = (maxScore+2)-(-0.5)
    plt.xlim([-0.5,maxScore+2])
    assert Qinfo["ypadding_fac"]>=1 , f'The padding factor should be greater or equal to 1: {Qinfo["ypadding_fac"]}'

    

    # Write fractional scores above the letter grade bars 
    for i,x,y in zip(range(len(lbars)),lbins[:-1],lbars):
        #txt = plt.text(x,y+0.03*dy,f' {y:.2f}',color='black',fontsize=9,va='center',ha='left')
        #txt.set_path_effects([PathEffects.withStroke(linewidth=1, foreground=lcolorbar[i])])
        #plt.text(x,y+0.02*dy,f'  {y:.2f}',color='black',fontsize=9)
        plt.text(x,y+0.015*dy,f' {y:.2f}',color=lcolorbar[i],fontsize=8)


    if(Qinfo["showLetters"]):
        # Letter grade divides 
        for i in range(1,len(lgrade)): 
            plt.plot([lbins[i],lbins[i]],[0,1],'k--',alpha=0.5)

        # Leter grades 
        for idx,val in enumerate(lgrade):
            xpos = 0.5*(lbins[idx]+lbins[idx+1])
            ypos = 0.5*(bar_max+ymax)
            writeLetterGrade(xpos,ypos,val,Qinfo)

    # Number of scores 
    plt.text(0.02*dx,0.925*ymax,f'$N=${numScore}',fontsize=10)

    # Stats  
    # =-=-=-==-=-=-==-=-=-==-=-=-==-=-=-=
    score_mean = np.mean(scores)
    score_median = np.median(scores)

    # Calculate max of scores 
    score_max = max(scores) 
    score_max_count = len(scores[scores==score_max])

    # Calculate mode(s) 
    ind_score_freq = [list(scores).count(i) for i in range(0,maxScore+1)]
    ind_score_num = list(range(0,maxScore+1))
    score_mode_freq = max(ind_score_freq)
    score_mode_ties = ind_score_freq.count(score_mode_freq)
    score_mode = [] 
    for i in range(score_mode_ties):
        idx = ind_score_freq.index(score_mode_freq)
        score_mode.append(ind_score_num[idx])
        ind_score_freq.pop(idx)
        ind_score_num.pop(idx) 

    # Put mode (\^M) above the relevant bars 
    if(Qinfo["showMode"]):
        for local_mode in score_mode:
            for mode_idx in range(len(bins)-1):
                if( (bins[mode_idx]<=local_mode) and (bins[mode_idx+1]>local_mode) ):
                    break 
            score_mid = 0.5*(bins[mode_idx] + bins[mode_idx+1])  # center of the bin
            yshift =  stat_shift*dy 
            if bars[mode_idx]+yshift < 0: 
                yshift = 0.03*dy  # don't go below bar
            plt.text(score_mid,bars[mode_idx] + yshift,r'$\^M$',fontsize=8,ha='center') #ASDF

    # Put Q2 above median 
    if(Qinfo["showMedian"]):
        for med_idx in range(len(bins)-1):
            if( (bins[med_idx]<=score_median) and (bins[med_idx+1]>score_median) ):
                break 
        score_mid = 0.5*(bins[med_idx] + bins[med_idx+1])  # center of the bin
        yshift =  stat_shift*dy 
        if bars[med_idx]+yshift < 0: 
            yshift = 0.03*dy  # don't go below bar
        plt.text(score_mid,bars[med_idx] + yshift,r'$Q_2$',fontsize=8,ha='center') #ASDF
        yshift_med = yshift 
        score_mid_med = score_mid  # save for later use

    # Put mu above mean 
    if(Qinfo["showMean"]):
        for mean_idx in range(len(bins)-1):
            if( (bins[mean_idx]<=score_mean) and (bins[mean_idx+1]>score_mean) ):
                break 
        score_mid = 0.5*(bins[mean_idx] + bins[mean_idx+1])  # center of the bin
        yshift =  stat_shift*dy 
        if bars[mean_idx]+yshift < 0: 
            yshift = 0.03*dy  # don't go below bar
        if(Qinfo["showMedian"] and score_mid == score_mid_med):
            yshift += 0.05*dy
        plt.text(score_mid,bars[mean_idx] + yshift,r'$\mu$',fontsize=8,ha='center') #ASDF
        #plt.plot([score_mid,score_mean+Qinfo['xtick_shift']],[0,bars[mean_idx]],'k--',alpha=0.4,lw=1)

    # Title alterations
    # =-=-=-==-=-=-==-=-=-==-=-=-==-=-=-=
    thetitle = title 
    if(Qinfo["showMean"]):
        thetitle += " , " + r'Mean $\mu$: ' + f'{score_mean:.1f}'

    if(Qinfo["showMedian"]):
        thetitle += " , " + r'Median $Q_2$: ' + f'{round(score_median,1)}'

    if(Qinfo["showMode"]):
        if(len(score_mode)>1):
            thetitle += " , " + r'Modes $\^M$: '
        else:
            thetitle += " , " + r'Mode $\^M$: '
        for idx,local_mode in enumerate(score_mode):
            thetitle += f'{int(local_mode)}'
            if(idx<len(score_mode)-1):
                thetitle += ', '
            
    if(Qinfo["showMax"]):
        thetitle += " , " + f'Max: {int(score_max)} ({score_max_count})'

    plt.title(thetitle,fontsize=9)


    # Tickmarks, if provided 
    # =-=-=-==-=-=-==-=-=-==-=-=-==-=-=-=
    if(len(tick_list[0])>0):
        xticks = np.array(tick_list[0])
    else:
        xticks = np.array(plt.gca().get_xticks())
    xticks = xticks[xticks>=0]
    xticks = xticks[xticks<=maxScore]
    plt.gca().set_xticks(xticks+Qinfo['xtick_shift'],[int(x) for x in xticks])

    if(len(tick_list[1])>0):
        yticks = np.array(tick_list[1])
    else:
        yticks = np.array(plt.gca().get_yticks())
    yticks = yticks[yticks>=0]
    yticks = yticks[yticks<=1]
    yticks = yticks[yticks<=ymax]
    plt.gca().set_yticks(yticks)

    
    # Cumulative score distribution 
    # =-=-=-==-=-=-==-=-=-==-=-=-==-=-=-=
    if(Qinfo["showCumulative_bars"] or Qinfo["showCumulative_scores"]):
        ax2 = plt.twinx()
        ax2.set_ylim([0,1.1])
        ax2.set_yticks([0,0.2,0.4,0.6,0.8,1.0])
        ax2.set_yticklabels([0,0.2,0.4,0.6,0.8,1.0],color=Qinfo["Cumulative_score_color"])
        ax2.spines['right'].set_color(Qinfo["Cumulative_score_color"])
        ax2.tick_params(axis='y',color=Qinfo["Cumulative_score_color"])
        ax2.set_ylabel('Cumulative Class Fraction',color=Qinfo["Cumulative_score_color"])

        # shift to center of bar 
        centers = bins[:-1] + 0.5*np.diff(bins) 

        if(Qinfo["showCumulative_bars"]):
            plt.plot(centers,cumbars,'-',linewidth=2,color=Qinfo["Cumulative_score_color"],alpha=0.5,zorder=0)
            plt.scatter(centers,cumbars,s=Qinfo["cumulative_ps"],facecolor='white',edgecolor='none',clip_on=False,zorder=1)
            plt.scatter(centers,cumbars,s=Qinfo["cumulative_ps"],facecolor=Qinfo["Cumulative_score_color"],alpha=0.5,clip_on=False,zorder=2)

        if(Qinfo["showCumulative_scores"]):
            score_cum = [scores[0]+Qinfo['xtick_shift']] + list(scores+Qinfo['xtick_shift'])
            score_frac = [0] + list(cumscores)
            plt.plot(score_cum,score_frac,'-',linewidth=2,color=Qinfo["Cumulative_score_color"],alpha=0.5,zorder=0)
            plt.scatter(score_cum[1:],score_frac[1:],s=Qinfo["cumulative_ps"],facecolor='white',edgecolor='none',clip_on=False,zorder=1)
            plt.scatter(score_cum[1:],score_frac[1:],s=Qinfo["cumulative_ps"],facecolor=Qinfo["Cumulative_score_color"],alpha=0.5,clip_on=False,zorder=2)

    if(outname is not None):
        plt.savefig(outname)
        print(f'Saved graph to {outname}')
        
        
    return() 



def gen_QuizCorrections(QuizInfo,frac_pts_returned,grade_bdys,shade_alpha,title,offset,outname=None):

    assert 0 < frac_pts_returned <= 1, f'Fraction of points returned should be between 0 and 1: {frac_pts_returned}'

    nQuestions = QuizInfo["numQuestions"]
    orig_score = np.arange(0,nQuestions+1,1)
    pts_returned = np.floor(frac_pts_returned*np.arange(nQuestions,-1,-1))
    new_score = orig_score + pts_returned 

    # Create figure 
    fig, ax = plt.subplots(1,2,sharey=True,figsize=(12,6)) 
    plt.subplots_adjust(wspace=0)

    # Line plots of original and new scores 
    ax[0].plot(orig_score,orig_score,'-o',color=SMC['red'],label='No Corrections',zorder=2)
    ax[0].plot(orig_score,new_score,'-o',color=SMC['canyon'],label='With Corrections',zorder=2)

    ax[0].set_xlabel("Original Score")
    ax[0].set_ylabel("New Score")
    ax[0].legend(loc=4,fontsize=9)

    # Title 
    plt_title = title
    ax[0].set_title(plt_title,fontsize=10)

    grade_bdys_sorted = list(grade_bdys.values())
    grade_bdys_sorted.sort() 
    grade_bdys_sorted.append(nQuestions)

    # Shade regions where grade remains unchanged 
    for gidx in range(len(grade_bdys_sorted)-1):
        left = grade_bdys_sorted[gidx]-offset 
        right = grade_bdys_sorted[gidx+1]-offset 
        top = grade_bdys_sorted[gidx+1]-offset 
        bot = grade_bdys_sorted[gidx]-offset 
        if(gidx==len(grade_bdys_sorted)-2):
            right += 2*offset 
            top += 2*offset 
        ax[0].fill_between([left,right],[top,top],[bot,bot],color=SMC['sun'],alpha=shade_alpha,linewidth=0)

    # Shade regions where grade improves (alpha<1 makes multiple letter grade changes darker colors 
    for grade_boost in range(1,len(grade_bdys)):

        for gidx in range(len(grade_bdys_sorted)-2):
            
            if(gidx+grade_boost>=len(grade_bdys_sorted)-1): 
                continue 
            
            left = grade_bdys_sorted[gidx]-offset 
            right = grade_bdys_sorted[gidx+1]-offset 
            top = grade_bdys_sorted[-1]+offset 
            bot = grade_bdys_sorted[gidx+grade_boost]-offset 
            if(gidx==len(grade_bdys_sorted)-2):
                right += 2*offset 
                top += 2*offset 

            ax[0].fill_between([left,right],[top,top],[bot,bot],color=SMC['water'],alpha=shade_alpha,linewidth=0)

    for idx,grd in enumerate(grade_bdys.keys()):
        left = grade_bdys_sorted[0]-0.5*offset
        top  = grade_bdys_sorted[-1-idx]-2*offset
        if(idx==0): 
            top += 2*offset
        ax[0].text(left,top,'+'+str(len(grade_bdys_sorted)-2-idx) + ' grade change',color='white',fontsize=12,ha='left',va='top',zorder=1)


    # Line plots of original and new scores 
    ax[1].plot(orig_score,orig_score,'-o',color=SMC['red'],label='No Corrections')
    ax[1].plot(orig_score,new_score,'-o',color=SMC['canyon'],label='With Corrections')

    ax[1].set_xlabel("Original Score")
    #ax[1].set_ylabel("New Score")
    #ax[1].legend(loc=4,fontsize=9)

    # Title 
    ax[1].set_title(f'Possible points returned: {frac_pts_returned*100:.1f}%',fontsize=10)


    # Shade regions where grade remains unchanged 
    for gidx in range(0,1):
        left = grade_bdys_sorted[gidx]-offset 
        right = grade_bdys_sorted[gidx+1]-offset 
        top = grade_bdys_sorted[gidx+1]-offset 
        bot = grade_bdys_sorted[gidx]-offset 
        if(gidx==len(grade_bdys_sorted)-2):
            right += 2*offset 
            top += 2*offset 
        ax[1].fill_between([left,right],[top,top],[bot,bot],color=SMC['garden'],alpha=shade_alpha,linewidth=0)


    # Shade regions based on new letter grade 
    for botshift in range(0,len(grade_bdys_sorted)-2):
        for gidx in range(botshift,len(grade_bdys_sorted)-2):
            
            left = grade_bdys_sorted[0]-offset 
            right = grade_bdys_sorted[2+gidx]-offset 
            bot = grade_bdys_sorted[gidx+1]-offset 
            top = grade_bdys_sorted[gidx+2]-offset 
            
            if(gidx==len(grade_bdys_sorted)-3):
                right += 2*offset 
                top += 2*offset 

            #plt.fill_between([left,right],[top,top],[bot,bot],color=SMC['bay'],alpha=0.4,linewidth=1)
            ax[1].fill_betweenx([bot,top],[right,right],[left,left],color=SMC['bay'],alpha=shade_alpha,linewidth=0)

    for idx,grd in enumerate(grade_bdys.keys()):
        left = grade_bdys_sorted[0]-0.5*offset
        top  = grade_bdys_sorted[-1-idx]-2*offset
        if(idx==0): 
            top += 2*offset
        ax[1].text(left,top,grd,color='white',fontsize=15,ha='left',va='top')


    if(outname is not None):
        print(f'Saving plot to file {outname}')
        plt.savefig(outname)

    return() 

def gen_ParticpationAvg(gbook,plot_info,title,outname=None):



    return

def gen_AssignmentAvg(gbook,plot_info,title,outname=None):


    return 



def gen_CorrelationScatter(data,maxScores,Qinfo,letters,labels,title,tick_lists,cbar=None,outname=None):

    # Optional data arrays
    # Third data becomes the color 
    # Fourth data becomes the size of the points

    assert len(data)>=2 , "Need at least two data arrays to plot a correlation scatter plot" 
    assert all(len(data[0])==len(d) for d in data), "All data arrays must have the same length"
    assert len(data)==len(labels), "Number of data arrays must match number of labels"



    plt.xlabel(labels[0])
    plt.ylabel(labels[1])
    plt.title(title,fontsize=Qinfo["title_fs"])
    plt.xlim([0,maxScores[0]])
    plt.ylim([0,maxScores[1]])
    plt.xticks(tick_lists[0],[int(x) for x in tick_lists[0]])
    plt.yticks(tick_lists[1],[int(x) for x in tick_lists[1]])
        
    plt.scatter(data[0],data[1],s=map_pointsize(data[3]) if len(data)>3 else Qinfo["scatter_ps"],alpha=Qinfo["scatter_alpha"],c=data[2] if len(data)>2 else 'black',edgecolor='black',linewidth=0.5)

    if(len(data)>2):
        plt.colorbar(label=labels[2],orientation='vertical')
        plt.clim(0,maxScores[2])  # Set color limits if color data is provided
        plt.clabel(labels[2],fontsize=Qinfo["cbar_fs"])



    if(outname is not None):
        print(f'Saving plot to file {outname}')
        plt.savefig(outname)

    return

def map_pointsize(data):

    data_array = np.array(data)
    data_max = max(data)
    data_min = min(data)

    if(data_max == data_min):
        return np.ones(len(data)) * 100
    else:
        # Normalize data to a range of 10 to 1000
        return np.interp(data_array, (data_min, data_max), (10, 1000))


