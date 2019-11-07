class Album:
    def __init__(this, name, year, tracks, length):
        this.name = name
        this.year = year
        this.tracks = tracks
        this.length = length

    def __lt__(this, other):
        return this.year<other.year

    def __str__(this):
        return "Name:\t{0}\nYear:\t{1}\nTracks:\t{2}\nLength:\t{3}\n________<3________".format(
            this.name, this.year, this.tracks, this.length
        )
