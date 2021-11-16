from numpy import __init__ as np


def streamfunction(var,dxy,dz,n_levs):
    buffer = np.zeros(var.shape)
    print (buffer.shape,dxy.shape,dz.shape)
    for i in range(1,n_levs-1,1):
        iz=n_levs-1-i
        buffer[iz]= buffer[iz+1] -1e-6 * var.isel(depth=iz).values* dxy.values * dz.isel(nav_lev=iz).values
    return  buffer


def osf_meridional(var,e1,e3,n_levs):
    buffer=streamfunction(var,e1,e3,n_levs)
    return np.array(buffer) #np.nansum(buffer,axis=2)


def osf_zonal(var,e2,e3,n_levs):
    buffer = streamfunction(var, e2, e3, n_levs)
    return np.array(buffer) # np.nansum(buffer,axis=1)


def zonalOC(ds, msk):

    e2 = msk.e2u.isel(time_counter=0)
    e3 = msk.e3u_0.isel(time_counter=0)

    u = ds.u[0]
    z_levs = ds.depth

    n_levs = len(z_levs)

    psi = osf_zonal(u, e2,e3,n_levs)

    land=np.copy(psi == 0)
    psi[land] = np.nan
    print(psi.shape,'psi')
    u*=np.nan
    u[:]=psi
    u=u.rename('zoc')
    return u


def meridionalOC(ds,msk):

    e1 = msk.e1v.isel(time_counter=0)
    e3 = msk.e3v_0.isel(time_counter=0)

    v = ds.v[0]
    z_levs = ds.depth
    n_levs = len(z_levs)

    psi = osf_meridional(v, e1,e3,n_levs)
    land=np.copy(psi == 0)
    psi[land] = np.nan

    v*=np.nan
    v[:]=psi
    v=v.rename('moc')
    return v