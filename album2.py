album = {'Orchid': {'Year': 1995, 'Songs': '8 songs', 'Length': '1 hr 11 min'}, \
'Morningrise': {'Year': 1996, 'Songs': '6 songs', 'Length': '1 hr 14 min'}}

for name, info in album.items():
    print("\nName:", info)

    for key in info:
        print (key + ':', info)
