import xarray as xr
from glob import glob
import os
from natsort import natsorted


def main():
    os.makedirs(outdir,exist_ok=True)
    for var in vars:
        print(var)
        for year in years:
            print (year)
            yearlyFiles=natsorted(glob(os.path.join(base,f_tmpl.format(var=var, year=year))))
            print (os.path.join(base,f_tmpl.format(var=var, year=year)))
            ds=xr.open_mfdataset(yearlyFiles,concat_dim='time')
            if var=='zoc':
                if not latBOX:
                    ds_sub=ds.sum(dim='lat',skipna=True)
                    ds_sub.mean(dim='time',skipna=True).to_netcdf(os.path.join(outdir,f'{var}_{year}.nc'))
                else:

                    ds_sub=ds.sel(lat=slice(latBOX[0],latBOX[1]))
                    ds_sub=ds_sub.sum(dim='lat',skipna=True)
                    ds_sub.mean(dim='time',skipna=True).to_netcdf(os.path.join(outdir,f'{var}_{year}_{latBOX[0]}-{latBOX[1]}.nc'))

            elif var=='moc':
                ds_sub=ds.sum(dim='lon',skipna=True)
                ds_sub.mean(dim='time',skipna=True).to_netcdf(os.path.join(outdir,f'{var}_{year}.nc'))





base='/work/opa/sc33616/nemo/tools/OC/daily_rean16_2D' # path to daily stream function file
f_tmpl='{var}_{year}*.nc'
outdir='yearlyOC_2D'

years=range(1993,2021,1)
vars=['moc', 'zoc']
lonBOX=False # please set list with [minlon, maxlon] if you need slicing data, or False to compute ZOC on the whole domain
latBOX= False # please set list with [minlon, maxlon] if you need slicing data, or False to compute MOC on the whole domain

if __name__ == '__main__':
    main()