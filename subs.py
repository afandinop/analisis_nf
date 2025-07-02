import numpy as np

def ptsinpoly(pflat, pflon, lat, lon):
    """
    Function to decide which points are inside or outside a user-defined polygon.
    
    Parameters:
    pflat : array-like
        Latitude vector defining the polygon points.
    pflon : array-like
        Longitude vector defining the polygon points.
    lat : array-like
        Latitude vector of points of interest.
    lon : array-like
        Longitude vector of points of interest.
    
    Returns:
    isave : list
        Indices of points (lat, lon) inside the polygon.
    """
    isave = []
    polsize = len(pflon)
    
    # Check if polygon is closed, if not, close it
    if pflon[0] != pflon[-1] or pflat[0] != pflat[-1]:
        pflon = np.append(pflon, pflon[0])
        pflat = np.append(pflat, pflat[0])
        polsize += 1
    
    # Define the number of points of interest
    pntssize = len(lon)
    
    # Conversion factor: radians to degrees
    radtodeg = 180 / np.pi
    
    # Iterate through each point of interest
    for j in range(pntssize):
        ang = []
        for i in range(polsize - 1):
            if lon[j] == pflon[i] and lat[j] == pflat[i]:
                ang.append(360)
            else:
                dx1 = lon[j] - pflon[i]
                dy1 = lat[j] - pflat[i]
                dx2 = lon[j] - pflon[i + 1]
                dy2 = lat[j] - pflat[i + 1]
                
                angle_diff = (np.arctan2(dy2, dx2) - np.arctan2(dy1, dx1)) * radtodeg
                
                if angle_diff > 180:
                    angle_diff -= 360
                elif angle_diff < -180:
                    angle_diff += 360
                
                ang.append(angle_diff)
        
        angsum = abs(sum(ang))
        
        # If the sum of angles is approximately 360, the point is inside
        if angsum >= 360 - 1:  # Allow for some small floating-point error
            isave.append(j)
   
        isave2 = np.array(isave,dtype=int)

    return isave2


