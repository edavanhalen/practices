album = {'Orchid': {'Year': 1995, 'Tracks': 8, 'Length': '1 hr 11 min'}, \
'Morningrise': {'Year': 1996, 'Tracks': 6, 'Length': '1 hr 14 min'}, \
'My Arms Your Hearse': {'Year': 1998, 'Tracks': 11, 'Length': '1 hr 2 min'}, \
'Still Life': {'Year': 1999, 'Tracks': 7, 'Length': '1 hr 2 min'}, \
'Blackwater Park': {'Year': 2000, 'Tracks': 9, 'Length': '1 hr 16 min'}, \
'Deliverance': {'Year': 2002, 'Tracks': 6, 'Length': '1 hr 1 min'}, \
'Damnation': {'Year': 2003, 'Tracks': 8, 'Length': '43 min'}, \
'Ghost Reveries': {'Year': 2005, 'Tracks': 8, 'Length': '1 hr 6 min'}, \
'Watershed': {'Year': 2008, 'Tracks': 10, 'Length': '1 hr 11 min' }, \
'Heritage': {'Year': 2011, 'Tracks': 10, 'Length': '56 min'}, \
'Pale Communion': {'Year': 2014, 'Tracks': 8, 'Length': '55 min'}, \
'Sorceress': {'Year': 2016, 'Tracks': 16, 'Length': '1 hr 30 min'}
}

for n, info in album.items():
    print("\nName:", n)

    for key in info:
        print (key + ':', info[key])
