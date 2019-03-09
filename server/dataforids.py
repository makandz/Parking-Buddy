datafile = open('trips.txt','r')
station_name = {}

for lines in datafile:
    datalines = lines.split(',')
    tripid = datalines[2]
    names = datalines[3]

    for names in datalines:
        if names in station_name:
            station_name[names] = station_name[names].append(tripid)
    else: 
      station_name[names] = [tripi]
  

datafile.close()
