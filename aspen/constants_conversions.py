from dataclasses import dataclass

import numpy as np
import numpy.typing as npt

@dataclass(frozen=True)
class PhysicsConstants:
    """
    A collection of fundamental physical constants, almost always in SI units.
    """

    # Gravity 
    # =-=-=-=-=-=--==-=-==-=-=-=-==-=-===-=-=-

    # Gravitational constant
    G_NEWTON: float = 6.67430e-11  # m^3 kg^-1 s^-2


    # Electromagnetism
    # =-=-=-=-=-=--==-=-==-=-=-=-==-=-===-=-=-

    # Speed of light in vacuum
    C_LIGHT: float = 299792458  # m/s

    # Faraday's constant
    FARADAY: float = 96485.3321233100184  # C/mol

    # Permitivity and Permeability of Free Space
    EPSILON_0: float = 8.8541878128e-12  # F/m
    MU_0: float = 1.2566370614e-6  # N/A^2

    # Coulomb's constant (8.9875517923e9)
    K_COULOMB: float = 1 / (4 * np.pi * EPSILON_0)  # N*m^2/C^2

    # Fundamental charge unit 
    E_CHARGE: float = 1.602176634e-19  # C


    # Thermodynamics
    # =-=-=-=-=-=--==-=-==-=-=-=-==-=-===-=-=-

    # Avogadro's number
    N_AVOGADRO: float = 6.02214076e23  # mol^-1

    # Boltzmann constant
    K_BOLTZMANN: float = 1.380649e-23  # J/K

    # Ideal gas constant
    R_GAS: float = 8.31446261815324  # J/(mol*K)


    # Quantum Mechanics
    # =-=-=-=-=-=--==-=-==-=-=-=-==-=-===-=-=-

    # Planck's constant
    H_PLANCK: float = 6.62607015e-34  # J*s 
    H_PLANCK_REDUCED: float = H_PLANCK / (2 * np.pi)  # J*s

    # Stefan-Boltzmann constant (5.670374419e-8)
    SB_CONSTANT: float = 2*np.pi**5*K_BOLTZMANN**4/(15*C_LIGHT**2*H_PLANCK**3)  # W/(m^2*K^4)

    # Radiation constant
    A_RADIATION: float = 4 * SB_CONSTANT / C_LIGHT  # J/(m^3*K^4)

    # Mass of protons, neutrons, and electrons
    # Source: CODATA 2018
    M_PROTON: float = 1.67262192369e-27  # kg
    M_NEUTRON: float = 1.67492749804e-27  # kg
    M_ELECTRON: float = 9.1093837015e-31  # kg

    # Atomic Mass Unit 
    AMU: float = 1.66053906660e-27  # kg

    # Bohr radius
    BOHR_RADIUS: float = 5.29177210903e-11  # m


@dataclass(frozen=True)
class ConversionsAndDerivedUnits:
    """
    Conversion factors and derived units. All are multiplicative factors unless noted in the name.
    """

    # Metric Prefixes (you don't have this memorized yet?)
    KILO: float = 1e3  # kilo (k)
    MEGA: float = 1e6  # mega (M)
    GIGA: float = 1e9  # giga (G)
    TERA: float = 1e12  # tera (T)
    PETA: float = 1e15  # peta (P)
    EXA: float = 1e18  # exa (E)
    CENTI: float = 1e-2  # centi (c)
    MILLI: float = 1e-3  # milli (m)
    MICRO: float = 1e-6  # micro (μ)
    NANO: float = 1e-9  # nano (n)
    PICO: float = 1e-12  # pico (p)
    FEMTO: float = 1e-15  # femto (f)
    ATTO: float = 1e-18  # atto (a)

    # Distances 
    METER_TO_ANGSTROM: float = 1e10  # m to Å
    ANGSTROM_TO_METER: float = 1 / METER_TO_ANGSTROM  # Å to m
    METER_TO_FOOT: float = 3.28084  # m to ft
    FOOT_TO_METER: float = 1 / METER_TO_FOOT  # ft to m
    INCH_TO_METER: float = 0.0254  # in to m
    METER_TO_INCH: float = 1 / INCH_TO_METER  # m to in
    INCH_TO_CM: float = 2.54  # in to cm
    CM_TO_INCH: float = 1 / INCH_TO_CM  # cm to in
    MILE_TO_KM: float = 1.60934  # mi to km
    KM_TO_MILE: float = 1 / MILE_TO_KM  # km to mi
    MILE_TO_METER: float = 1609.34  # mi to m
    METER_TO_MILE: float = 1 / MILE_TO_METER  # m to mi

    # Magnetic fields 
    GAUSS_TO_TESLA: float = 1e-4  # G to T
    TESLA_TO_GAUSS: float = 1 / GAUSS_TO_TESLA  # T to G


    # Times 
    YEAR_TO_SECOND: float = 365.25 * 24 * 3600  # yr to s
    SECOND_TO_YEAR: float = 1 / YEAR_TO_SECOND  # s to yr
    DAY_TO_SECOND: float = 24 * 3600  # day to s
    SECOND_TO_DAY: float = 1 / DAY_TO_SECOND  # s to day
    MINUTE_TO_SECOND: float = 60  # min to s
    SECOND_TO_MINUTE: float = 1 / MINUTE_TO_SECOND  # s to min
    GYR_TO_SECOND: float = 1e9 * YEAR_TO_SECOND  # Gyr to s
    SECOND_TO_GYR: float = 1 / GYR_TO_SECOND  # s to Gyr

    # Energies 
    EV_TO_JOULE: float = 1.602176634e-19  # eV to J
    JOULE_TO_EV: float = 1 / EV_TO_JOULE  # J to eV
    ERG_TO_JOULE: float = 1e-7  # erg to J
    JOULE_TO_ERG: float = 1 / ERG_TO_JOULE  # J to erg
    CALORIE_TO_JOULE: float = 4.184  # cal to J
    JOULE_TO_CALORIE: float = 1 / CALORIE_TO_JOULE  # J to cal
    BTU_TO_JOULE: float = 1055.06  # BTU to J
    JOULE_TO_BTU: float = 1 / BTU_TO_JOULE  # J to BTU
    KILOCAL_TO_JOULE: float = 4184  # kcal to J
    JOULE_TO_KILOCAL: float = 1 / KILOCAL_TO_JOULE  # J to kcal

    # Angles 
    DEGREE_TO_RADIAN: float = np.pi / 180  # degree to rad
    RADIAN_TO_DEGREE: float = 1 / DEGREE_TO_RADIAN  # rad to degree
    GRADIAN_TO_RADIAN: float = np.pi / 200  # grad to rad
    RADIAN_TO_GRADIAN: float = 1 / GRADIAN_TO_RADIAN  # rad to grad

    # Masses 
    LBS_TO_KG: float = 0.453592  # lbs to kg
    KG_TO_LBS: float = 1 / LBS_TO_KG  # kg to lbs

    # Temperatures 
    KELVIN_TO_CELSIUS_ADD: float = -273.15  # K to °C
    CELSIUS_TO_KELVIN_ADD: float = -KELVIN_TO_CELSIUS_ADD  # °C to K

    # Pressures 
    ATM_TO_PASCAL: float = 101325  # atm to Pa
    PASCAL_TO_ATM: float = 1 / ATM_TO_PASCAL  # Pa to atm

    # Volumes 
    LITER_TO_CUBIC_METER: float = 0.001  # L to m^3
    CUBIC_METER_TO_LITER: float = 1 / LITER_TO_CUBIC_METER  # m^3 to L
    GALLON_TO_LITER: float = 3.78541  # gal to L
    LITER_TO_GALLON: float = 1 / GALLON_TO_LITER  # L to gal

    # Angles 
    ARCSEC_TO_RADIAN: float = 4.84814e-6  # arcsec to rad
    RADIAN_TO_ARCSEC: float = 1 / ARCSEC_TO_RADIAN  # rad to arcsec
    ARCMIN_TO_RADIAN: float = 2.9088e-4  # arcmin to rad
    RADIAN_TO_ARCMIN: float = 1 / ARCMIN_TO_RADIAN  # rad to arcmin
    ARCSEC_TO_DEGREE: float = 2.77778e-4  # arcsec to degree
    DEGREE_TO_ARCSEC: float = 1 / ARCSEC_TO_DEGREE  # degree to arcsec

    # Converting SI units to CGS units

    # Length
    LENGTH_SI_TO_CGS: float = 1e2  # m to cm
    LENGTH_CGS_TO_SI: float = 1 / LENGTH_SI_TO_CGS  # cm to m
    # Time
    TIME_SI_TO_CGS: float = 1  # s to s
    TIME_CGS_TO_SI: float = 1 / TIME_SI_TO_CGS  # s to s
    # Mass
    MASS_SI_TO_CGS: float = 1e3  # kg to g
    MASS_CGS_TO_SI: float = 1 / MASS_SI_TO_CGS  # g to kg
    # Energy
    ENERGY_SI_TO_CGS: float = 1e3  # J to erg
    ENERGY_CGS_TO_SI: float = 1 / ENERGY_SI_TO_CGS  # erg to J
    # Force
    FORCE_SI_TO_CGS: float = 1e5  # N to dyn
    FORCE_CGS_TO_SI: float = 1 / FORCE_SI_TO_CGS  # dyn to N
    # Power
    POWER_SI_TO_CGS: float = 1e7  # W to erg/s
    POWER_CGS_TO_SI: float = 1 / POWER_SI_TO_CGS  # erg/s to W
    # Pressure
    PRESSURE_SI_TO_CGS: float = 1e-6  # Pa to dyne/cm^2
    PRESSURE_CGS_TO_SI: float = 1 / PRESSURE_SI_TO_CGS  # dyne/cm^2 to Pa
    # Magnetic field
    MAGNETIC_FIELD_SI_TO_CGS: float = 1e4  # T to G
    MAGNETIC_FIELD_CGS_TO_SI: float = 1 / MAGNETIC_FIELD_SI_TO_CGS  # G to T
    # Electric field
    ELECTRIC_FIELD_SI_TO_CGS: float= 1e3  # V/m to statV/cm
    ELECTRIC_FIELD_CGS_TO_SI: float = 1 / ELECTRIC_FIELD_SI_TO_CGS  # statV/cm to V/m
    # Capacitance
    CAPACITANCE_SI_TO_CGS: float = 1e-9  # F to statF
    CAPACITANCE_CGS_TO_SI: float = 1 / CAPACITANCE_SI_TO_CGS  # statF to F
    # Inductance
    INDUCTANCE_SI_TO_CGS: float = 1e-3  # H to statH
    INDUCTANCE_CGS_TO_SI: float = 1 / INDUCTANCE_SI_TO_CGS  # statH to H
    # Charge
    CHARGE_SI_TO_CGS: float = 1e-3  # C to statC
    CHARGE_CGS_TO_SI: float = 1 / CHARGE_SI_TO_CGS  # statC to C
    # Current
    CURRENT_SI_TO_CGS: float = 1e-3  # A to statA
    CURRENT_CGS_TO_SI: float = 1 / CURRENT_SI_TO_CGS  # statA to A
    # Magnetic flux
    MAGNETIC_FLUX_SI_TO_CGS: float = 1e-3  # Wb to maxwell
    MAGNETIC_FLUX_CGS_TO_SI: float = 1 / MAGNETIC_FLUX_SI_TO_CGS  # maxwell to Wb
    # Electric potential
    ELECTRIC_POTENTIAL_SI_TO_CGS: float = 1e-3  # V to statV
    ELECTRIC_POTENTIAL_CGS_TO_SI: float = 1 / ELECTRIC_POTENTIAL_SI_TO_CGS  # statV to V
    # Induced voltage
    INDUCED_VOLTAGE_SI_TO_CGS: float = 1e-3  # V to statV
    INDUCED_VOLTAGE_CGS_TO_SI: float = 1 / INDUCED_VOLTAGE_SI_TO_CGS  # statV to V


@dataclass(frozen=True)
class WorldData: 
    """
    World data constants
    """

    # Population of the USA and world
    USA_POPULATION: float = 333.3e6  # people 
    WORLD_POPULATION: float = 7.9e9  # people

    # Area of the world
    USA_AREA: float = 9.8e6 * (1000**2)  # m^2
    WORLD_AREA: float = 510.1e6 * (1000**2)  # m^2

    # Density of the world 
    USA_POP_AREADEN: float = USA_POPULATION / USA_AREA  # people/m^2
    WORLD_POP_AREADEN: float = WORLD_POPULATION / WORLD_AREA  # people/m^2


@dataclass(frozen=True)
class AstroConstantsAndUsefulNumbers:
    """
    Astronomical constants and conversions. All in SI units unless noted in the name (e.g., P_EARTH_DAY = 365.25).
    
    Exceptions:
    Angles are in degrees.
    Some values are in their commonly used units (e.g., Hubble constant in km/s/Mpc).
    """

    # Astronomical Unit (AU)
    AU: float = 149597870700  # meters

    # Parsec (pc)
    PARSEC: float = 3.08567758149137e16  # meters

    # Light year (ly)
    LIGHT_YEAR: float = 9.4607304725808e15  # meters

    # Solar and Sidereal time
    SOLAR_DAY: float = 24 * 3600  # seconds
    SIDEREAL_DAY: float = 23 * 3600 + 56 * 60 + 4.0916  # seconds, time to rotate 2pi 
    SOLAR_YEAR: float = 365.25 * 24 * 3600  # seconds
    SIDEREAL_YEAR: float = 365.256363004 * 24 * 3600  # seconds

    # Stellar parameters of the Sun 
    M_SUN: float = 1.9891e30  # kg
    R_SUN: float = 6.957e8  # meters
    L_SUN: float = 3.828e26  # Watts
    DEN_SUN: float = 1.41e3  # kg/m^3
    T_SUN: float = 5772  # Kelvin
    TC_SUN: float = 1.571e7  # Kelvin
    B_SUN: float = 1e-4  # Tesla
    G_SUN: float = 1.36e3  # W/m^2 (Solar constant) 
    MU_SUN: float = M_SUN * PhysicsConstants.G_NEWTON  # m^3/s^2 (Solar parameter)
    AGE_SUN: float = 4.6e9 * 365.25 * 24 * 3600  # seconds (age of the Sun)

    # Rocky planet parameters of the Earth 
    M_EARTH: float = 5.972e24  # kg
    R_EARTH: float = 6.371e6  # meters
    B_EARTH: float = 5e-5  # Tesla
    DEN_EARTH: float = 5.51e3  # kg/m^3

    # Gas giant parameters of Jupiter 
    M_JUPITER: float = 1.898e27  # kg
    R_JUPITER: float = 7.1492e7  # meters
    B_JUPITER: float = 4e-4  # Tesla
    DEN_JUPITER: float = 1.33e3  # kg/m^3

    # Moon parameters 
    M_MOON: float = 7.34767309e22  # kg
    R_MOON: float = 1.7374e6  # meters
    DEN_MOON: float = 3.34e3  # kg/m^3

    # Orbital Parameters of Earth
    A_EARTH: float = 1.496e11  # meters (semi-major axis)
    E_EARTH: float = 0.0167  # eccentricity
    I_EARTH: float = 0  # degrees (orbit inclination relative to the ecliptic)
    P_EARTH_DAY: float = 365.256363004  # days (orbital period)
    ROI_EARTH: float = 23.45  # degrees (rotation axis orientation relative to the ecliptic)

    # Orbital Parameters of Jupiter 
    A_JUPITER: float = 7.785e11  # meters (semi-major axis)
    E_JUPITER: float = 0.0489  # eccentricity
    I_JUPITER: float = 1.303  # degrees (orbit inclination relative to the ecliptic)
    P_JUPITER_DAY: float = 4332.589  # days (orbital period)
    ROI_JUPITER: float = 3.13  # degrees (rotation axis orientation relative to the ecliptic)

    # Orbital Parameters of Moon 
    A_MOON: float = 3.844e8  # meters (semi-major axis)
    E_MOON: float = 0.0549  # eccentricity
    I_MOON: float = 5.145  # degrees (orbit inclination relative to the ecliptic)
    P_MOON_DAY: float= 27.321661  # days (orbital period)
    ROI_MOON: float = 1.53  # degrees (rotation axis orientation relative to the ecliptic)

    # Milky Way parameters (check these)
    MW_RADIUS: float = 5.0e4 * LIGHT_YEAR  # meters (radius of Milky Way)
    MW_MASS: float = 1.5e12 * M_SUN  # kg (mass of Milky Way)
    MW_LUMINOSITY: float = 5e10 * L_SUN  # Watts (luminosity of Milky Way)
    MW_BRIGHTNESS: float = MW_LUMINOSITY / (4 * np.pi * MW_RADIUS**2)  # W/m^2 (brightness of Milky Way)
    MW_SCALE_LENGTH: float = 1.5e4 * LIGHT_YEAR  # meters (scale length of Milky Way)

    # Cosmological Parameters
    H0_HUBBLE: float = 70  # km/s/Mpc (Hubble constant)
    OMEGA_M: float = 0.3150  # matter density parameter
    OMEGA_LAMBDA: float = 0.6849  # dark energy density parameter
    OMEGA_K: float = 0  # curvature density parameter
    OMEGA_RADIATION: float = 0.0001  # radiation density parameter

    HUBBLE_RADIUS: float = PhysicsConstants.C_LIGHT / H0_HUBBLE  # meters (Hubble radius)
    HUBBLE_TIME: float = 1 / H0_HUBBLE  # seconds (Hubble time)

    T_CMB: float = 2.72548  # Kelvin (CMB temperature)
    AGE_UNIVERSE: float = 13.8e9 * 365.25 * 24 * 3600  # seconds (age of the universe)
    R_UNIVERSE: float = 46.508e9 * 3.08567758149137e16  # meters (radius of observable universe)

    # Solar System Data 
    M_SOLAR_SYSTEM_ARR: npt.NDArray[np.float64] = \
        np.array([0.33,4.87,M_EARTH/1e24,0.642,M_JUPITER/1e24,568,86.8,102,0.013])*1e24 # kg
    A_SOLAR_SYSTEM_AU_ARR: npt.NDArray[np.float64] = \
        np.array([0.387,0.723,1.0,1.524,5.203,9.537,19.191,30.069,39.482]) # AU  
    E_SOLAR_SYSTEM_ARR: npt.NDArray[np.float64] = \
        np.array([0.205,0.006,00.0167,0.093,0.048,0.054,0.047,0.0086,0.248]) # eccentricity
    P_SOLAR_SYSTEM_YR_ARR: npt.NDArray[np.float64] = \
        np.array([0.24,0.62,1,1.88,11.86,29.46,84.01,164.8,248.6]) # years 
    R_SOLAR_SYSTEM_ARR: npt.NDArray[np.float64] = \
        0.5*np.array([4879,12104,12742,6779,139822,116464,50724,49244,2376])*1e3 # radius, meters 
    MEAN_ANOM_SOLAR_SYSTEM_ARR: npt.NDArray[np.float64] = \
        np.array([174.79, 50.44, 0, 19.412, 19.65, -42.48, 142.26, 259.90, 14.53]) # mean ano, degrees 

    NAMES_SOLAR_SYSTEM_LIST: list[str] = ["Mercury","Venus","Earth","Mars","Jupiter","Saturn","Uranus","Neptune","Pluto"]
