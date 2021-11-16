from glob import glob
import os
import xarray as xr
from OC import zonalOC, meridionalOC
from nemoReader import Nemo


def ZOC(base,msk,outdir, NEMOtype):
    grid = 'U'
    filledPath = base.format(grid=grid)

    allfiles=glob(filledPath)
    for f in allfiles:
        print (f)
        day=os.path.basename(f).split('_')[-1]
        nemo_ds = Nemo(f)
        ds=getattr(nemo_ds,NEMOtype)()

        zoc= zonalOC(ds, msk)
        zoc.to_netcdf(os.path.join(outdir,'zoc_{day}'.format(day=day)))

def MOC(base, msk, outdir, NEMOtype):
    grid = 'V'
    filledPath = base.format(grid=grid)

    allfiles = glob(filledPath)
    for f in allfiles:
        day = os.path.basename(f).split('_')[-1]
        print(f)
        nemo_ds = Nemo(f)
        ds = getattr(nemo_ds, NEMOtype)()

        moc = meridionalOC(ds, msk)
        moc.to_netcdf(os.path.join(outdir, 'moc_{day}.nc'.format(day=day)))


def main():
    os.makedirs(outdir,exist_ok=True)
    msk = xr.open_dataset(mask_path)
    ZOC(base, msk, outdir, input_type)
    MOC(base, msk,outdir, input_type)



base='/path_to_dailyFiles/nemo_grid_{grid}_*.nc'
mask_path='/path/to/nemo_mesh_mask.nc'
outdir='daily_OC_2D'
input_type= 'from_v3' # available options 'from_v3','from_v4','from_medv3', 'from_pqTool', 'from_CFcompl'


if __name__ == '__main__':
    main()