# nemo_OC


- set variables in getOCfiles2D.py

base='/path_to_dailyFiles/filename_{grid}_*.nc'
base is the path to the files. Please consider that:
 files need to be daily
 the filename must declare the grid type , U or V. The code search for U or V in {grid}

mask_path='/path/to/nemo_mesh_mask.nc'
mask_path is the path to the nemo mesh mask

outdir='daily_OC_2D'

outdir is the directory where the files will be stored. If not exists, will be created

input_type= 'from_v3'
input_type is used from the nemo module to call functions
available options are:
'from_v3' if the nemo files comes from NEMO v3* version
'from_v4' if the nemo files comes from NEMO v4* version
'from_medv3' if the nemo files comes from the CMEMS MED-PHY
'from_pqTool' if the nemo files comes from CMCC-PQtool
'from_CFcompl' if the nemo files are CF compliant

- run command
python getOCfiles2D.py


# compute yearly OC
- set variables in computeYearly2D.py

base='path/to/dailyOCfiles'
base id the path to daily stream function file produced by  getOCfiles2D.py

f_tmpl='{var}_{year}*.nc'
f_tmpl is the template for the files in base. No needs changes if user is using the standard output name from getOCfiles2D

outdir='yearlyOC_2D'
outdir is the directory where the files will be stored. If not exists, will be created

years=range(startingYear,EndYear+1,1)
years is the list of years user need

vars=['moc', 'zoc']
vars is a list. User can select one or both 'moc' and 'zoc'

lonBOX=False
lonBOX allow to compute ZOC on the whole domain (if False), or on a reduced domain (set list with [minlon, maxlon])

latBOX= False
latBOX allow to compute MOC on the whole domain (if False), or on a reduced domain (set list with [minlat, maxlat])

- run command
python computeYearly2D.py