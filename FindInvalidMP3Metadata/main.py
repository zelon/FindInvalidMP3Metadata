#!/usr/bin/python
# -*- coding:utf-8 -*-


'''
Created on 2012. 2. 19.

@author: zelon

if unicode exception occur, modify setencoding() from encoding = "ascii" to "utf-8" in /usr/lib/python2.7/site.py

'''

import os

# if you use ubuntu, you can install eyeD3 using apt-get install python-eyed3
import eyeD3

def hasValidCharacter(checkString):
    
    checkMeangless = ["AudioTrack", "no artist", "no title", 'none']
    
    for meaning in checkMeangless:
        if checkString.lower().find(meaning.lower()) != -1:
            return False
    
    uniString = unicode(checkString)
    
    for u in uniString:
        
        # normal ascii http://www.asciitable.com/
        if u >= ' ' and u <= '~':
            pass
        elif u == '♬':
            pass
        elif u >= 'a' and u <= 'z':
            pass
        elif u >= 'A' and u <= 'Z':
            pass
        elif u >= '0' and u <= '9':
            pass
        elif u >= unicode('가', "utf-8") and u <= unicode('힣', "utf-8"):
            #print("has korean")
            pass
        # refer to http://ko.wikipedia.org/wiki/%EC%9C%A0%EB%8B%88%EC%BD%94%EB%93%9C_%EB%B2%94%EC%9C%84_%EB%AA%A9%EB%A1%9D
        elif u >= u'\u4E00' and u <= u'\u9FBF':
            #print("has hanja")
            pass
        elif u >= u'\uf900' and u <= u'\ufaff':
            #print("has CJK compatible hanja")
            pass
        elif u >= u'\u3040' and u <= u'\u309f':
            #print("has hiragana")
            pass
        elif u >= u'\u30a0' and u <= u'\u30ff':
            #print("has katakana")
            pass
        elif u in ['〈', '〉', '＆' , '！', '／', '…', '♡', '：', '’']:
            pass
        elif u in [ ',', ' ', '.', "\'", '[', ']', '(', ')', '-', '~', '!', '#', '&', '`', '?', '+', ':', '/', '<', '>', '$']:
            #print("has here")
            pass
        else:
            return False

    return True

def checkValid(filename):

    tag = eyeD3.Tag()
    
    info = "Filename : " + filename
    
    result = True
    artist = None
    album = None
    title = None

    try:
        tag.link(unicode(filename, "utf-8"))
    except Exception, ex:
        print("Exception : " + str(ex));
        info += "link exception" + "\n"
        result = False

    if result == True:
        artist = tag.getArtist()
        album = tag.getAlbum()
        title = tag.getTitle()
    
        try:
            if hasValidCharacter(artist) == False or hasValidCharacter(album) == False or hasValidCharacter(title) == False:
                result = False
        except UnicodeDecodeError, ex:
            result = False
    
    if result == False:
        
        print("-----------------------------")
        print(info)
        print("Artist : "),
        print(artist)
        print("Album : "),
        print(album)
        print("Title : "),
        print(title)
        pass

def isCheckingFilename(filename):
    
    f = filename.lower()
    
    if f[-4:] == ".jpg":
        return False
    
    return True    

def testmain(folder):

    checkingfilecount = 0
    
    for root, dirs, files in os.walk(folder):
        for filename in files:
            fullname = root + "/" + str(filename) 
            
            if isCheckingFilename(filename):
                checkValid(fullname)            
    
    print("Checked file count : " + str(checkingfilecount))
                
if __name__ == '__main__':
    testmain("/home/zelon/drives/P/MyMusic")
