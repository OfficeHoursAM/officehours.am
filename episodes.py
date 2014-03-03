entries = [
    {
        "title": "The Microtransaction Generation",
        "description": "Office Hours' pilot episode, wherein Patrick and Ryan sit down with Alec Davis to discuss the death of careers, so-called \"2-sided markets,\" opportunism in the face of a shaky economy, generational identity, the globalization of communities, and the responsibility of opportunists in this new way of operating.\n\nThis month's articles:\n\nMatchmaker, Matchmaker, Find Me a Part-Time Job - NPR (http://www.npr.org/2012/05/31/154009061/matchmaker-matchmaker-find-me-a-part-time-job)\nCareers Are Dead. Welcome to Your Low-Wage, Temp Work Future - Forbes (http://www.forbes.com/sites/jmaureenhenderson/2012/08/30/careers-are-dead-welcome-to-your-low-wage-temp-work-future/)\nFor Ridesharing Apps Like Lyft, Commerce is a Community - WUNC/NPC (http://wunc.org/post/ridesharing-apps-lyft-commerce-community)\nPeer-to-peer rental: The rise of the sharing economy - The Economist (http://www.economist.com/news/leaders/21573104-internet-everything-hire-rise-sharing-economy)",
        "length": 97472596,
        "duration": "48:26",
        "pubdate": "Mon, 3 Mar 2014 10:00:00 -0500",
        "guest":
        {
            "name": "Alec Davis",
            "href": "http://twitter.com/alecat1008"
        }
    }
]

def filenames():
    return ["ep%d.m4a" % entryIndex for entryIndex in range(len(entries))]

# fileURLFormat = "https://s3.amazonaws.com/officehours.am/%s"
fileURLFormat = "https://dl.dropboxusercontent.com/u/2338382/distro/%s"
