## Pogdesign TV Calendar Sync ##
![](http://i.imgur.com/kdSx2ry.png)

**pogdesign-sync** is a simple addon for Kodi/XBMC. It automatically scans your whole TV Shows database and synchronize watched episodes with your [http://www.pogdesign.co.uk/cat/](http://www.pogdesign.co.uk/cat/) calendar (TVC).

### Intro ###
You may ask why I even bother with a TV calendar that doesn't have a proper name and domain (pogdesign WTF?). Isn't Trakt.tv better? Probably it is, but I've been using TVC for years now and I love it. It's fast, simple, clean and reliable. Even with Kodi + SickRage I'm still checking TVC to see what shows has been released and I'm marking those episodes that I've watched.

*Please note that I'm not a professional developer and it was my first encounter with Python/Kodi. Addon is so simple that it can't breake anything, but it might not work properly in 100% situations.*

### Features ###
Brace yourself because the addon is just feature-rich! Here we go:

1. Scan Kodi's library and automatically mark watched episodes on [http://www.pogdesign.co.uk/cat/](http://www.pogdesign.co.uk/cat/) calendar.

It's a one way synchronization - script selects only watched episodes from Kodi's database and marks them as watched on the online calendar. It does NOT go in the opposite direction. Also it does NOT unmark unwatched episodes.

Synchronization is performed when:

- Kodi has been launched.
- Video library has been refreshed.

**Compatibility:**

Addon was tested on Kodi 14.2 Helix for Windows and on OpenELEC 5.95.2 for RaspberryPi 2. It should work on other versions, becasue it doesn't need any dependencies.


### How to use it ###
1. Download .zip from here - [Download](https://github.com/rafakob/service.pogdesign.sync/archive/master.zip)
2. Unpack it and edit in Notepad file **service.py**
3. Go to lines 8, 9 and type your USERNAME and PASS for the TVC. Save the file.
4. Repack folder once again into .zip. It should looks like [this](http://i.imgur.com/fOmhjJj.png).
5. In Kodi go to *Settings > Add-ons > Install from zip file* > Choose created zip file.
6. That's all. Addon will work in background. It doesn't display any notifications.


### Future plans ###
- Simple GUI for editing settings.
- Short notifications when calendar has been synced.
- Web scraping optimization.
- Full two way sync (configurable).
- Perform sync on finish watching episode.

I know how to do most of the things, I just need some time.

### Changelog ###
    0.1.0
	- Initial working version
