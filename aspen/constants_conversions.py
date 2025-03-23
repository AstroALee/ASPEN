

import numpy as np 


class PHYSICS:
    """
    Physical constants and conversions
    """

    # Gravity 
    # =-=-=-=-=-=--==-=-==-=-=-=-==-=-===-=-=-

    # Gravitational constant
    G_NEWTON = 6.67430e-11  # m^3 kg^-1 s^-2


    # Electromagnetism 
    # =-=-=-=-=-=--==-=-==-=-=-=-==-=-===-=-=-

    # Speed of light in vacuum
    C_LIGHT = 299792458  # m/s

    # Faraday's constant
    FARADAY = 96485.3321233100184  # C/mol

    # Permitivity and Permeability of free space
    EPSILON_0 = 8.854187817e-12  # F/m
    MU_0 = 1.2566370614e-6  # N/A^2

    # Coulomb's constant (8.9875517923e9)
    K_COULOMB = 1 / (4 * np.pi * EPSILON_0)  # N*m^2/C^2

    # Fundamental charge unit 
    E_CHARGE = 1.602176634e-19  # C


    # Thermodynamics
    # =-=-=-=-=-=--==-=-==-=-=-=-==-=-===-=-=-

    # Avogadro's number
    N_AVOGADRO = 6.02214076e23  # mol^-1

    # Boltzmann constant
    K_BOLTZMANN = 1.380649e-23  # J/K

    # Ideal gas constant
    R_GAS = 8.31446261815324  # J/(mol*K)


    # Quantum Mechanics
    # =-=-=-=-=-=--==-=-==-=-=-=-==-=-===-=-=-

    # Planck's constant
    H_PLANCK = 6.62607015e-34  # J*s 
    H_PLANCK_REDUCED = H_PLANCK / (2 * np.pi)  # J*s

    # Stefan-Boltzmann constant (5.670374419e-8)
    SB_CONSTANT = 2*np.pi**5*K_BOLTZMANN**4/(15*C_LIGHT**2*H_PLANCK**3)  # W/(m^2*K^4)

    # Radiation constant
    A_RADIATION = 4 * SB_CONSTANT / C_LIGHT  # J/(m^3*K^4)

    # Mass of protons, neutrons, and electrons
    # Source: CODATA 2018
    M_PROTON = 1.67262192369e-27  # kg
    M_NEUTRON = 1.67492749804e-27  # kg
    M_ELECTRON = 9.1093837015e-31  # kg

    # Atomic Mass Unit 
    AMU = 1.66053906660e-27  # kg

    # Bohr radius
    BOHR_RADIUS = 5.29177210903e-11  # m




class CONVERSIONS:
    """
    Conversion factors and derived units 
    """

    # Metric Prefixes (you don't have this memorized yet?)
    KILO = 1e3  # kilo (k)
    MEGA = 1e6  # mega (M)
    GIGA = 1e9  # giga (G)
    TERA = 1e12  # tera (T)
    PETA = 1e15  # peta (P)
    EXA = 1e18  # exa (E)
    CENTI = 1e-2  # centi (c)
    MILLI = 1e-3  # milli (m)
    MICRO = 1e-6  # micro (μ)
    NANO = 1e-9  # nano (n)
    PICO = 1e-12  # pico (p)
    FEMTO = 1e-15  # femto (f)
    ATTO = 1e-18  # atto (a)

    # Distances 
    METER_TO_ANGSTROM = 1e10  # m to Å
    ANGSTROM_TO_METER = 1 / METER_TO_ANGSTROM  # Å to m
    METER_TO_FOOT = 3.28084  # m to ft
    FOOT_TO_METER = 1 / METER_TO_FOOT  # ft to m
    INCH_TO_METER = 0.0254  # in to m
    METER_TO_INCH = 1 / INCH_TO_METER  # m to in
    INCH_TO_CM = 2.54  # in to cm
    CM_TO_INCH = 1 / INCH_TO_CM  # cm to in
    MILE_TO_KM = 1.60934  # mi to km
    KM_TO_MILE = 1 / MILE_TO_KM  # km to mi
    MILE_TO_METER = 1609.34  # mi to m
    METER_TO_MILE = 1 / MILE_TO_METER  # m to mi

    # Times 
    YEAR_TO_SECOND = 365.25 * 24 * 3600  # yr to s
    SECOND_TO_YEAR = 1 / YEAR_TO_SECOND  # s to yr
    DAY_TO_SECOND = 24 * 3600  # day to s
    SECOND_TO_DAY = 1 / DAY_TO_SECOND  # s to day
    MINUTE_TO_SECOND = 60  # min to s
    SECOND_TO_MINUTE = 1 / MINUTE_TO_SECOND  # s to min
    GYR_TO_SECOND = 1e9 * YEAR_TO_SECOND  # Gyr to s
    SECOND_TO_GYR = 1 / GYR_TO_SECOND  # s to Gyr

    # Energies 
    EV_TO_JOULE = 1.602176634e-19  # eV to J
    JOULE_TO_EV = 1 / EV_TO_JOULE  # J to eV
    ERG_TO_JOULE = 1e-7  # erg to J
    JOULE_TO_ERG = 1 / ERG_TO_JOULE  # J to erg

    # Masses 
    LBS_TO_KG = 0.453592  # lbs to kg
    KG_TO_LBS = 1 / LBS_TO_KG  # kg to lbs

    # Temperatures 
    KELVIN_TO_CELSIUS_ADD = -273.15  # K to °C
    CELSIUS_TO_KELVIN_ADD = -KELVIN_TO_CELSIUS_ADD  # °C to K

    # Pressures 
    ATM_TO_PASCAL = 101325  # atm to Pa
    PASCAL_TO_ATM = 1 / ATM_TO_PASCAL  # Pa to atm

    # Volumes 
    LITER_TO_CUBIC_METER = 0.001  # L to m^3
    CUBIC_METER_TO_LITER = 1 / LITER_TO_CUBIC_METER  # m^3 to L
    GALLON_TO_LITER = 3.78541  # gal to L
    LITER_TO_GALLON = 1 / GALLON_TO_LITER  # L to gal

    # Angles 
    ARCSEC_TO_RADIAN = 4.84814e-6  # arcsec to rad
    RADIAN_TO_ARCSEC = 1 / ARCSEC_TO_RADIAN  # rad to arcsec
    ARCMIN_TO_RADIAN = 2.9088e-4  # arcmin to rad
    RADIAN_TO_ARCMIN = 1 / ARCMIN_TO_RADIAN  # rad to arcmin
    ARCSEC_TO_DEGREE = 2.77778e-4  # arcsec to degree
    DEGREE_TO_ARCSEC = 1 / ARCSEC_TO_DEGREE  # degree to arcsec




class WORLD_DATA: 
    """
    World data constants
    """

    # Population of the USA and world
    USA_POPULATION = 333.3e6  # people 
    WORLD_POPULATION = 7.9e9  # people

    # Area of the world
    USA_AREA = 9.8e6 * (1000**2)  # m^2
    WORLD_AREA = 510.1e6 * (1000**2)  # m^2

    # Density of the world 
    USA_POP_AREADEN = USA_POPULATION / USA_AREA  # people/m^2
    WORLD_POP_AREADEN = WORLD_POPULATION / WORLD_AREA  # people/m^2




class ASTRO:
    """
    Astronomical constants and conversions
    """

    # Astronomical Unit (AU)
    AU = 149597870700  # meters

    # Parsec (pc)
    PARSEC = 3.08567758149137e16  # meters

    # Light year (ly)
    LIGHT_YEAR = 9.4607304725808e15  # meters

    # Solar and Sidereal time
    SOLAR_DAY = 24 * 3600  # seconds
    SIDEREAL_DAY = 23 * 3600 + 56 * 60 + 4.0916  # seconds, time to rotate 2pi 

    # Stellar parameters of the Sun 
    M_SUN = 1.9891e30  # kg
    R_SUN = 6.957e8  # meters
    L_SUN = 3.828e26  # Watts
    DEN_SUN = 1.41e3  # kg/m^3
    T_SUN = 5772  # Kelvin
    TC_SUN = 1.571e7  # Kelvin
    B_SUN = 1e-4  # Tesla
    G_SUN = 1.36e3  # W/m^2 (Solar constant) 
    MU_SUN = M_SUN * PHYSICS.G_NEWTON  # m^3/s^2 (Solar parameter)
    AGE_SUN = 4.6e9 * 365.25 * 24 * 3600  # seconds (age of the Sun)

    # Rocky planet parameters of the Earth 
    M_EARTH = 5.972e24  # kg
    R_EARTH = 6.371e6  # meters
    B_EARTH = 5e-5  # Tesla
    DEN_EARTH = 5.51e3  # kg/m^3

    # Gas giant parameters of Jupiter 
    M_JUPITER = 1.898e27  # kg
    R_JUPITER = 7.1492e7  # meters
    B_JUPITER = 4e-4  # Tesla
    DEN_JUPITER = 1.33e3  # kg/m^3

    # Moon parameters 
    M_MOON = 7.34767309e22  # kg
    R_MOON = 1.7374e6  # meters
    DEN_MOON = 3.34e3  # kg/m^3

    # Orbital Parameters of Earth
    A_EARTH = 1.496e11  # meters (semi-major axis)
    E_EARTH = 0.0167  # eccentricity
    I_EARTH = 0  # degrees (orbit inclination relative to ecliptic)
    P_EARTH = 365.256363004  # days (orbital period)
    ROI_EARTH = 23.45  # degrees (rotation axis orientation relative to ecliptic)

    # Orbital Parameters of Jupiter 
    A_JUPITER = 7.785e11  # meters (semi-major axis)
    E_JUPITER = 0.0489  # eccentricity
    I_JUPITER = 1.303  # degrees (orbit inclination relative to ecliptic)
    P_JUPITER = 4332.589  # days (orbital period)
    ROI_JUPITER = 3.13  # degrees (rotation axis orientation relative to ecliptic)

    # Orbital Parameters of Moon 
    A_MOON = 3.844e8  # meters (semi-major axis)
    E_MOON = 0.0549  # eccentricity
    I_MOON = 5.145  # degrees (orbit inclination relative to ecliptic)
    P_MOON = 27.321661  # days (orbital period)
    ROI_MOON = 1.53  # degrees (rotation axis orientation relative to ecliptic)

    # Cosmological Parameters
    H0_HUBBLE = 70  # km/s/Mpc (Hubble constant)
    OMEGA_M = 0.3150  # matter density parameter
    OMEGA_LAMBDA = 0.6849  # dark energy density parameter
    OMEGA_K = 0  # curvature density parameter
    OMEGA_RADIATION = 0.0001  # radiation density parameter

    HUBBLE_RADIUS = PHYSICS.C_LIGHT / H0_HUBBLE  # meters (Hubble radius)
    HUBBLE_TIME = 1 / H0_HUBBLE  # seconds (Hubble time)

    T_CMB = 2.72548  # Kelvin (CMB temperature)
    AGE_UNIVERSE = 13.8e9 * 365.25 * 24 * 3600  # seconds (age of the universe)
    R_UNIVERSE = 46.508e9 * 3.08567758149137e16  # meters (radius of observable universe)

    # Solar System Data 
    M_SOLAR_SYSTEM_ARR = np.array([0.33,4.87,M_EARTH/1e24,0.642,M_JUPITER/1e24,568,86.8,102,0.013])*1e24, # kg
    A_SOLAR_SYSTEM_ARR = np.array([0.387,0.723,1.0,1.524,5.203,9.537,19.191,30.069,39.482]), # AU  
    E_SOLAR_SYSTEM_ARR = np.array([0.205,0.006,00.0167,0.093,0.048,0.054,0.047,0.0086,0.248]), # eccentricity
    P_SOLAR_SYSTEM_ARR = np.array([0.24,0.62,1,1.88,11.86,29.46,84.01,164.8,248.6]), # years 
    R_SOLAR_SYSTEM_ARR = 0.5*np.array([4879,12104,12742,6779,139822,116464,50724,49244,2376])*1e3, # radius, meters 
    MEAN_ANOM_SOLAR_SYSTEM_ARR = np.array([174.79, 50.44, 0, 19.412, 19.65, -42.48, 142.26, 259.90, 14.53]), # mean ano, degrees 
    NAMES_SOLAR_SYSTEM_ARR = ["Mercury","Venus","Earth","Mars","Jupiter","Saturn","Uranus","Neptune","Pluto"],
