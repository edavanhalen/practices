from datetime import timedelta

class Album:
    def __init__(this, name, year, tracks, length):
        length_words = length.split()
        h = int(length_words[0])
        m = int(length_words[2])
        this.name = name
        this.year = year
        this.tracks = int(tracks.split()[0])
        this.length = timedelta(minutes=m, hours=h)

    def __str__(this):
        return ("Name:\t{0}\nYear:\t{1}\nTracks:\t{2}\nLength:\t{3}\n________<3________".format(
            this.name, this.year, this.tracks, this.length
        ))

    def __lt__(this, other):
        return (this.year<other.year)

    def ucuk(self):
        return self.year**2/self.length.seconds

albums = [
    Album( 'Orchid', 1995, '8 tracks', '1 hr 11 min'),
    Album( 'Morningrise', 1996, '6 tracks', '1 hr 14 min'),
    Album( 'My Arms Your Hearse', 1998, '11 tracks', '1 hr 2 min'),
    Album( 'Still Life', 1999, '7 tracks', '1 hr 2 min'),
    Album( 'Blackwater Park', 2000, '9 tracks', '1 hr 16 min'),
    Album( 'Deliverance', 2002, '6 tracks', '1 hr 1 min' ),
    Album( 'Damnation', 2003,'8 tracks', '0 hr 43 min'),
    Album( 'Ghost Reveries', 2005, '8 tracks', '1 hr 6 min'),
    Album( 'Watershed', 2008, '10 tracks', '1 hr 11 min'),
    Album( 'Heritage', 2011, '10 tracks', '0 hr 56 min'),
    Album( 'Pale Communion', 2014, '8 tracks', '0 hr 55 min'),
    Album( 'Sorceress', 2016, '16 tracks', '1 hr 30 min')
]

if __name__ == "__main__":
    albums.sort(key = lambda i: i.tracks, reverse=True)
    for i in albums:
        print(i)

    albums.sort()
    for i in albums:
        print(i)