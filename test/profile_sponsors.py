import instaloader

L = instaloader.Instaloader()
L.load_session_from_file("yourUsername")

def printSponsors():
    profileData = instaloader.Profile.from_username(L.context, "targetUsername")
    for profile in profileData.get_sponsors():
        print(profile.username)

if __name__ == "__main__":
    printSponsors()