album = {'Orchid': {'Year': 1995, 'Tracks': 8, 'Length': '1 hr 11 min'}, \
'Morningrise': {'Year': 1996, 'Tracks': 6, 'Length': '1 hr 14 min'}}

for n, info in album.items():
    print("\nName:", n)

    for key in info:
        print (key + ':', info[key])
