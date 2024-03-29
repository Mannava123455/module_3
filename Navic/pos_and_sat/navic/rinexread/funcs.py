
import pytest
import xarray
from pytest import approx
import georinex as gr
from datetime import datetime, timedelta
import numpy as np
import pandas as pd
import math
import itertools
import argparse




def navic(file):
    df = pd.read_csv(file)
    l=len(df)
    sv = [0]*l#df ['sv'].tolist()
    time=[0]*l
    month=[0]*l
    day =[0]*l
    hour=[0]*l
    minute =[0]*l
    second=[0]*l
    SVclockBias = df['SVclockBias'].tolist()
    SVclockDrift = df['SVclockDrift'].tolist()
    SVclockDriftRate = df['SVclockDriftRate'].tolist()
    IODEC = df['IODEC'].tolist()
    Crs = df['Crs'].tolist()
    DeltaN = df['DeltaN'].tolist()
    M0 = df['M0'].tolist()
    Cuc = df['Cuc'].tolist()
    Eccentricity = df['Eccentricity'].tolist()
    Cus = df['Cus'].tolist()
    sqrtA = df['sqrtA'].tolist()
    Toe = df['Toe'].tolist()
    Cic = df['Cic'].tolist()
    Omega0 = df['Omega0'].tolist()
    Cis = df['Cis'].tolist()
    Io = df['Io'].tolist()
    Crc = df['Crc'].tolist()
    omega = df['omega'].tolist()
    OmegaDot = df['OmegaDot'].tolist()
    IDOT = df['IDOT'].tolist()
    codesL2 = [0]*l
    BDTWeek = df['BDTWeek'].tolist()
    L2flag = [0]*l
    URA = df['URA'].tolist()
    health = df['health'].tolist()
    TGD = df['TGD'].tolist()
    IODC =[0]*l
    TransTime = df['TransTime'].tolist()
    
    
    data = list([[a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z,aa,ab,ac,ad,ae,af,ag,ah,ai,] for a, b, c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z,aa,ab,ac,ad,ae,af,ag,ah,ai in list(zip(sv,time,month,day,hour,minute,second,SVclockBias,SVclockDrift,SVclockDriftRate,IODEC,Crs,DeltaN,M0,Cuc,Eccentricity,Cus,sqrtA,Toe,Cic,Omega0,Cis,Io,Crc,omega,OmegaDot,IDOT,codesL2,BDTWeek,L2flag,URA,health,TGD,IODC,TransTime))])
    return data
