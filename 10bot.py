# -*- coding: utf-8 -*-
#SERK_TEAM

import LINETCR
from LINETCR.lib.curve.ttypes import *
import Wikipedia
from datetime import datetime
import time,random,sys,json,codecs,threading,glob,subprocess

cl = LINETCR.LINE()
print "#Serk_Bot"
cl.login(qr=True)
cl.loginResult()
print "Serkl-Login Success\n"

ki = LINETCR.LINE()
print "#Serk_Bot"
ki.login(qr=True)
ki.loginResult()
print "Serk2-Login Success\n"

ki2 = LINETCR.LINE()
print "#Serk_Bot"
ki2.login(qr=True)
ki2.loginResult()
print "Serk3-Login Success\n"

ki3 = LINETCR.LINE()
print "#Serk_Bot"
ki3.login(qr=True)
ki3.loginResult()
print "Serk4-Login Success\n"

ki4 = LINETCR.LINE()
print "#Serk_Bot"
ki4.login(qr=True)
ki4.loginResult()
print "Serk5-Login Success\n"

ki5 = LINETCR.LINE()
print "#Serk_Bot"
ki5.login(qr=True)
ki5.loginResult()
print "Serk6-Login Success\n"

ki6 = LINETCR.LINE()
print "#Serk_Bot"
ki6.login(qr=True)
ki6.loginResult()
print "Serk7-Login Success\n"

ki7 = LINETCR.LINE()
print "#Serk_Bot"
ki7.login(qr=True)
ki7.loginResult()
print "Serk8-Login Success\n"

print "〘=====[Serk Sukses All Login]=====〙"
reload(sys)
sys.setdefaultencoding('utf-8')

helpMessage =""" 
____________________|||____________________
|||________🍁***[~S͟͟͟͞͞͞E͟͟͟͞͞͞R͟͟͟͞͞͞K͟͟͟͞͞͞*B͟͟͟͞͞͞O͟͟͟͞͞͞T͟͟͟͞͞͞~]***🍁________||||
|||_________________|||________________||||

❂͜͡☆➣ [Id]
❂͜͡☆➣ [Mid]
❂͜͡☆➣ [Mc @]
❂͜͡☆➣ [Mc: @]
❂͜͡☆➣ [Me] 
❂͜͡☆➣ [TL 「Text」
❂͜͡☆➣ [MyName]
❂͜͡☆➣ [I Gift]
❂͜͡☆➣ [Mid 「mid」
❂͜͡☆➣ [List group] 
❂͜͡☆➣ [Glist] 
❂͜͡☆➣ [Group id]
❂͜͡☆➣ [Gcreator] 
❂͜͡☆➣ [Creator]
❂͜͡☆➣ [album 「id」]
❂͜͡☆➣ [Hapus album 「id」
❂͜͡☆➣ [Gcancel]
❂͜͡☆➣ [Jam say]
❂͜͡☆➣ [Up]
❂͜͡☆➣ [Bladd]
❂͜͡☆➣ [Bldell]
❂͜͡☆➣ [Ban:on] 
❂͜͡☆➣ [Unban:on]
❂͜͡☆➣ [Banlist]
❂͜͡☆➣ [Com on]
❂͜͡☆➣ [Com set]
❂͜͡☆➣ [Mcheck] 
❂͜͡☆➣ [ Message Confirmation] 
❂͜͡☆➣ [Mybio: 「Isi Bio」]  
❂͜͡☆➣ [Allbio: 「Isi Bio bot」] 
  
 🐯Command In Group🐯

❂͜͡☆➣ [Cipok/Ats@Tagall]
❂͜͡☆➣ [Lurking on]
❂͜͡☆➣ [Lurking]
❂͜͡☆➣ [Invite「Send contatc] 
❂͜͡☆➣ [Invite「mid」] 
❂͜͡☆➣ [Kmid: Kick by mid] 
❂͜͡☆➣ [Ginfo] 
❂͜͡☆➣ [Cancel]
❂͜͡☆➣ [Backup]
❂͜͡☆➣ [Gro ups]
❂͜͡☆➣ [Gn 「Nama grup」
❂͜͡☆➣ [Gurl]
❂͜͡☆➣ [gurl「kelompok ID
❂͜͡☆➣ [Nk「@」]
❂͜͡☆➣ [NK:]
❂͜͡☆➣ [Sory @]
❂͜͡☆➣ [Ban:]
❂͜͡☆➣ [Unban:]
❂͜͡☆➣ [Masuk]
❂͜͡☆➣ [Pulang]

    ☆ ٴ☬   SET BOT    ☬  ☆ 

❂͜͡☆➣ [Link on/off]
❂͜͡☆➣ [Contact on/off] 
❂͜͡☆➣ [Auto join on/off] 
❂͜͡☆➣ [Auto leave on/off] 
❂͜͡☆➣ [Auto add on/off] 
❂͜͡☆➣ [Jam on/off]
❂͜͡☆➣ [Like on/off]
❂͜͡☆➣ [Protect on/off]
❂͜͡☆➣ [qrprotect on/off]
❂͜͡☆➣ [Inviteprotect on/off]
❂͜͡☆➣ [Cancelprotect on/off]
❂͜͡☆➣ [Allprotect on/off]
❂͜͡☆➣ [Mprotect on/off]

🐯COMMAND Bot🐯

❂͜͡☆➣ Mybot
❂͜͡☆➣ [Q/.]
❂͜͡☆➣ [Pulang/..]
❂͜͡☆➣ S1-6 in
❂͜͡☆➣ S1-6 bye
❂͜͡☆➣ S1-6 
❂͜͡☆➣ S1-6name:
❂͜͡☆➣ Bye me
❂͜͡☆➣ Response
❂͜͡☆➣ Ry bye
❂͜͡☆➣ Papay
❂͜͡☆➣ BotStikers{Hore,Lol,No,Sue,Njiir,Tanks,Ok}
  
    ☆ ٴ☬   SELF  BOT    ☬  ☆ 

               􀜁􀇔 [ By.̶✍me̶̶ ✈ ] 
    [ http://line.me/ti/p/~rd.rmdhn ]
     
"""
helo=""

KAC=[cl,ki,ki2,ki3,ki4,ki5,ki6,ki7]
mid = cl.getProfile().mid
kimid = ki.getProfile().mid
ki2mid = ki2.getProfile().mid
ki3mid = ki3.getProfile().mid
ki4mid = ki4.getProfile().mid
ki5mid = ki5.getProfile().mid
ki5mid = ki5.getProfile().mid
ki6mid = ki6.getProfile().mid
ki7mid = ki7.getProfile().mid
Bots=[mid,kimid,ki2mid,ki3mid,ki4mid,ki5mid,ki6mid,ki7mid,"ucbd1374cb68242824dc21abcd7d6f669","u3fa0c0964985cd663d1fce84507e9b9b"]
admin = ["ucbd1374cb68242824dc21abcd7d6f669","u3fa0c0964985cd663d1fce84507e9b9b"]
staff = ["ucbd1374cb68242824dc21abcd7d6f669","u3fa0c0964985cd663d1fce84507e9b9b"]
adminMID = ["ucbd1374cb68242824dc21abcd7d6f669","u3fa0c0964985cd663d1fce84507e9b9b"]

wait = {
    'contact':False,
    'autoJoin':False,
    'autoCancel':{"on":True,"members":1},
    'leaveRoom':True,
    'timeline':True,
    'autoAdd':True,
    'message':"Owner : line://ti/p/~rd.rmdhn",
    "lang":"JP",
    "comment":"Owner : line://ti/p/~rd,rmdhn",
    "likeOn":True,
    "commentOn":True,
    "commentBlack":{},
    "wblack":False,
    "dblack":False,
    "clock":False,
    "cName1":" ᎦᏋᖇᏦ~ᏰᏫᎿ~1 ",
    "cName2":" ᎦᏋᖇᏦ~ᏰᏫᎿ~2 ",
    "cName3":" ᎦᏋᖇᏦ~ᏰᏫᎿ~3 ",
    "cName4":" ᎦᏋᖇᏦ~ᏰᏫᎿ~4 ",
    "cName5":" ᎦᏋᖇᏦ~ᏰᏫᎿ~5 ",
    "cName6":" ᎦᏋᖇᏦ~ᏰᏫᎿ~6 ",
    "cName7":" ᎦᏋᖇᏦ~ᏰᏫᎿ~7 ",
    "cName8":" ᎦᏋᖇᏦ~ᏰᏫᎿ~8 ",
    "blacklist":{},
    "wblacklist":False,
    "dblacklist":False,
    "Backup":True,
    "protect":True,
    "cancelprotect":False,
    "inviteprotect":False,
    "linkprotect":False,
    "atjointicket":True,
    "MProtection":True,
    #"ProtectQR":True,
    "Allprotect":False,
}


def cms(string, commands): #/XXX, &gt;XXX, ;XXX, ^XXX, %XXX, $XXX...
    tex = ["+","@","/","&gt;",";","^","%","$","＾","サテラ:","サテラ:","サテラ：","サテラ："]
    for texX in tex:
        for command in commands:
            if string ==command:
                return True
    return False

wait2 = {
    'readPoint':{},
    'readMember':{},
    'setTime':{},
    'ROM':{}
    }

setTime = {}
setTime = wait2['setTime']


contact = cl.getProfile()
backup = cl.getProfile()
backup.displayName = contact.displayName
backup.statusMessage = contact.statusMessage
backup.pictureStatus = contact.pictureStatus


def mention(to,nama):
    aa = ""
    bb = ""
    strt = int(12)
    akh = int(12)
    nm = nama
    #print nm
    for mm in nm:
      akh = akh + 2
      aa += """{"S":"""+json.dumps(str(strt))+""","E":"""+json.dumps(str(akh))+""","M":"""+json.dumps(mm)+"},"""
      strt = strt + 6
      akh = akh + 4
      bb += "\xe2\x98\xbb @x \n"
    aa = (aa[:int(len(aa)-1)])
    msg = Message()
    msg.to = to
    msg.from_ = profile.mid
    msg.text = "[MENTION]\n"+bb
    msg.contentMetadata ={'MENTION':'{"MENTIONEES":['+aa+']}','EMTVER':'4'}
    #print msg
    try:
       cl.sendMessage(msg)
    except Exception as error:
        print error
#-----------------------------------------------#
def sendMessage(to, text, contentMetadata={}, contentType=0):
    mes = Message()
    mes.to, mes.from_ = to, profile.mid
    mes.text = text
    mes.contentType, mes.contentMetadata = contentType, contentMetadata
    if to not in messageReq:
        messageReq[to] = -1
    messageReq[to] += 1
    #--------------------INVITE_INTO_ROOM--------------------
        if op.type == 21:
            cl.leaveRoom(op.param1)
            
            if 'MENTION' in msg.contentMetadata.keys() != None:
              if wait["detectMention"] == True:
                    contact = cl.getContact(msg.from_)
                    cName = contact.displayName
                    balas = ["Dont Tag Me!! Im Busy",cName + " Ngapain Ngetag?",cName + " Nggak Usah Tag-Tag! Kalo Penting Langsung Pc Aja","-_-"]
                    ret_ = "[Auto Respond] " + random.choice(balas)
                    name = re.findall(r'@(\w+)', msg.text)
                    mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                    mentionees = mention['MENTIONEES']
                    for mention in mentionees:
                           if mention['M'] in Bots:
                                  cl.sendText(msg.to,ret_)

def NOTIFIED_ACCEPT_GROUP_INVITATION(op):
    #print op
        if op.type == 17:
           if op.param2 in Bots:
              return
           ginfo = cl.getGroup(op.param1)
           random.choice(KAC).sendText(op.param1, "Hallo " + cl.getContact(op.param2).displayName)
           random.choice(KAC).sendText(op.param1, "Selamat Datang Di Grup  " + str(ginfo.name))
           random.choice(KAC).sendText(op.param1, "Creator Grup " + str(ginfo.name) + " :\n" + ginfo.creator.displayName)
           random.choice(KAC).sendText(op.param1, "Budayakan Baca Note yah Ka 😊\nSemoga Betah Kk 😘")
           random.choice(KAC).sendText(op.param1, "Silahkan Patuhi Peraturan & Jangan Nakal Ya!!!")  

def NOTIFIED_KICKOUT_FROM_GROUP(op):
    try:
        cl.sendText(op.param1, cl.getContact(op.param3).displayName + " Jangan Main Kick!\n(/*´･ω･*\)")
    except Exception as e:
        print e
        print ("\n\nNOTIFIED_KICKOUT_FROM_GROUP\n\n")
        return

def NOTIFIED_LEAVE_GROUP(op):
    try:
        cl.sendText(op.param1, cl.getContact(op.param2).displayName + " Babay\n(*´･ω･*)")
        random.choice(KAC).sendText(op.param1, "Good Bye" + "Semoga Tenang Disana")
    except Exception as e:
        print e
        print ("\n\nNOTIFIED_LEAVE_GROUP\n\n")
        return
#-----------------------------------------------
def bot(op):
    try:
        if op.type == 0:
            return
        if op.type == 13:
            if mid in op.param3:
                G = cl.getGroup(op.param1)
                if wait["autoJoin"] == True:
                    if wait["autoCancel"]["on"] == True:
                        if len(G.members) <= wait["autoCancel"]["members"]:
                            cl.rejectGroupInvitation(op.param1)
                        else:
                            cl.acceptGroupInvitation(op.param1)
                    else:
                        cl.acceptGroupInvitation(op.param1)
                elif wait["autoCancel"]["on"] == True:
                    if len(G.members) <= wait["autoCancel"]["members"]:
                        cl.rejectGroupInvitation(op.param1)
            else:
                Inviter = op.param3.replace("",',')
                InviterX = Inviter.split(",")
                matched_list = []
                for tag in wait["blacklist"]:
                    matched_list+=filter(lambda str: str == tag, InviterX)
                if matched_list == []:
                    pass
                else:
                    cl.cancelGroupInvitation(op.param1, matched_list)

        #if op.type == 15:
            #random.choice(KAC).sendText(op.param1, "Good Bye :)")
            #print op.param3 + "has left the group"

        #if op.type == 17:
            #group = ki2.getGroup(op.param1)
            #cb = Message()
            #cb.to = op.param1
            #cb.text = ki2.getContact(op.param2).displayName + " Selamat Datang di " + group.name
            #ki2.sendMessage(cb)
            
        if op.type == 55:
            print "[NOTIFIED_READ_MESSAGE]"
            try:
                if op.param1 in wait2['readPoint']:
                    Name = cl.getContact(op.param2).displayName
                    if Name in wait2['readMember'][op.param1]:
                        pass
                    else:
                        wait2['readMember'][op.param1] += "\n・" + Name + "\n " + datetime.today().strftime(' [%d - %H:%M:%S]')
                        wait2['ROM'][op.param1][op.param2] = "・" + Name
                        wait2['setTime'][msg.to] = datetime.today().strftime('%Y-%m-%d %H:%M:%S')
                else:
                    pass
            except:
                pass

        if op.type == 26:
            msg = op.message
            try:
                if msg.contentType == 0:
                    try:
                        if msg.to in wait2['readPoint']:
                            if msg.from_ in wait2["ROM"][msg.to]:
                                del wait2["ROM"][msg.to][msg.from_]
                        else:
                            pass
                    except:
                        pass
                else:
                    pass

            except KeyboardInterrupt:
                sys.exit(0)
            except Exception as error:
                print error
                print ("\n\nRECEIVE_MESSAGE\n\n")
                return         
        if op.type == 19:
            if mid in op.param3:
                wait["blacklist"][op.param2] = True
        if op.type == 22:
            if wait["leaveRoom"] == True:
                cl.leaveRoom(op.param1)
        if op.type == 24:
            if wait["leaveRoom"] == True:
                cl.leaveRoom(op.param1)
        if op.type == 26:
            msg = op.message
            if msg.toType == 0:
                msg.to = msg.from_
                if msg.from_ == "uca18eee00eac5c7fb779abf073d85126":
                    if "join:" in msg.text:
                        list_ = msg.text.split(":")
                        try:
                            cl.acceptGroupInvitationByTicket(list_[1],list_[2])
                            G = cl.getGroup(list_[1])
                            G.preventJoinByTicket = True
                            cl.updateGroup(G)
                        except:
                            cl.sendText(msg.to,"error")
            if msg.toType == 1:
                if wait["leaveRoom"] == True:
                    cl.leaveRoom(msg.to)
            if msg.contentType == 16:
                url = msg.contentMetadata["postEndUrl"]
                cl.like(url[25:58], url[66:], likeType=1001)
        if op.type == 26:
            elif "@"+cl.getProfile().displayName in msg.text:
                tanya = msg.text.replace("@"+cl.getProfile().displayName,"")
                jawab = ("Jgn Tag Si "+cl.getProfile().displayName+"!!","Berisik jgn tag si "+cl.getProfile().displayName+" dia masih tidur")
                jawaban = random.choice(jawab)
                cl.sendText(msg.to,jawaban)
        if "Setbio:" in msg.text:
          string = msg.text.replace("Setbio:","")
          if len(string.decode('utf-8')) <= 100000000000000000:
              profile = client.getProfile()
              profile.statusMessage = string
              client.updateProfile(profile)
              client.sendMessage(msg.to,"Update Bio Done")
          else:
              pass                              
        if wait["winvite"] == True:
                     if msg.from_ in admin:
                         _name = msg.contentMetadata["displayName"]
                         invite = msg.contentMetadata["mid"]
                         groups = cl.getGroup(msg.to)
                         pending = groups.invitee
                         targets = []
                         for s in groups.members:
                             if _name in s.displayName:
                                 k3.sendText(msg.to,"-> " + _name + " was here")
                                 break
                             elif invite in wait["blacklist"]:
                                 ki.sendText(msg.to,"Sorry, " + _name + " On Blacklist")
                                 k4.sendText(msg.to,"Call my daddy to use command !, \n➡Unban: " + invite)
                                 break                            
                             else:
                                 targets.append(invite)
                         if targets == []:
                             pass
                         else:
                             for target in targets:
                                 try:
                                     cl.findAndAddContactsByMid(target)
                                     cl.inviteIntoGroup(msg.to,[target])
                                     cl.sendText(msg.to,"Invited this nigga💋: \n➡" + _name)
                                     wait["winvite"] = False
                                     break
                                 except:
                                     try:
                                         ki.findAndAddContactsByMid(invite)
                                         ki.inviteIntoGroup(op.param1,[invite])
                                         wait["winvite"] = False
                                     except:
                                         try:
                                             k3.findAndAddContactsByMid(invite)
                                             k3.inviteIntoGroup(op.param1,[invite])
                                             wait["winvite"] = False
                                             k3.sendText(msg.to,"Suck`es hahahahaha💋: \n➡" + _name)
                                             break
                                         except:
                                            try:
                                                 k4.findAndAddContactsByMid(invite)
                                                 k4.inviteIntoGroup(op.param1,[invite])
                                                 wait["winvite"] = False
                                                 k4.sendText(msg.to,"DONE BABY 💋 \n➡" + _name)
                                                 break
                                            except:
                                                 cl.sendText(msg.to,"Negative, Error detected")
                                                 wait["winvite"] = False
                                                 break
        if op.type == 25:
            msg = op.message
            if msg.contentType == 13:
                if wait["wblack"] == True:
                    if msg.contentMetadata["mid"] in wait["commentBlack"]:
                        cl.sendText(msg.to,"sudah masuk daftar hitam👈")
                        wait["wblack"] = False
                    else:
                        wait["commentBlack"][msg.contentMetadata["mid"]] = True
                        wait["wblack"] = False
                        cl.sendText(msg.to,"Itu tidak berkomentar👈")
                if wait["akaInvite"] == True:
                     if msg.from_ in admin:
                         _name = msg.contentMetadata["displayName"]
                         invite = msg.contentMetadata["mid"]
                         groups = cl.getGroup(msg.to)
                         pending = groups.invitee
                         targets = []
                         for s in groups.members:
                             if _name in s.displayName:
                                 ki.sendText(msg.to,"-> " + _name + " was here")
                                 break
                             elif invite in wait["blacklist"]:
                                 ki.sendText(msg.to,"Sorry, " + _name + " On Blacklist")
                                 ki.sendText(msg.to,"Call my daddy to use command !, \n➡ Unban: " + invite)
                                 break
                             else:
                                 targets.append(invite)
                         if targets == []:
                             pass
                         else:
                             for target in targets:
                                 try:
                                     ki.findAndAddContactsByMid(target)
                                     ki.inviteIntoGroup(msg.to,[target])
                                     random.choice(KAC).sendText(msg.to,"✍⎯Serk__Ȿ⟿ℬᝪᝨ⟿☬ Invited: \n➡ " + _name)
                                     wait["akaInvite"] = False
                                     break
                                 except:
                                          cl.sendText(msg.to,"Negative, Err0r Detected")
                                          wait["akaInvite"] = False
                                          break
                elif wait["dblack"] == True:
                    if msg.contentMetadata["mid"] in wait["commentBlack"]:
                        del wait["commentBlack"][msg.contentMetadata["mid"]]
                        cl.sendText(msg.to,"Done")
                        wait["dblack"] = False
                    else:
                        wait["dblack"] = False
                        cl.sendText(msg.to,"Tidak ada dalam daftar hitam👈")
                elif wait["wblacklist"] == True:
                    if msg.contentMetadata["mid"] in wait["blacklist"]:
                        cl.sendText(msg.to,"sudah masuk daftar hitam")
                        wait["wblacklist"] = False
                    else:
                        wait["blacklist"][msg.contentMetadata["mid"]] = True
                        wait["wblacklist"] = False
                        cl.sendText(msg.to,"Done👈")
                elif wait["dblacklist"] == True:
                    if msg.contentMetadata["mid"] in wait["blacklist"]:
                        del wait["blacklist"][msg.contentMetadata["mid"]]
                        cl.sendText(msg.to,"Done👈")
                        wait["dblacklist"] = False
                    else:
                        wait["dblacklist"] = False
                        cl.sendText(msg.to,"Done👈")
                elif wait["contact"] == True:
                    msg.contentType = 0
                    cl.sendText(msg.to,msg.contentMetadata["mid"])
                    if 'displayName' in msg.contentMetadata:
                        contact = cl.getContact(msg.contentMetadata["mid"])
                        try:
                            cu = cl.channel.getCover(msg.contentMetadata["mid"])
                        except:
                            cu = ""
                        cl.sendText(msg.to,"[displayName]:\n" + msg.contentMetadata["displayName"] + "\n[mid]:\n" + msg.contentMetadata["mid"] + "\n[statusMessage]:\n" + contact.statusMessage + "\n[pictureStatus]:\nhttp://dl.profile.line-cdn.net/" + contact.pictureStatus + "\n[coverURL]:\n" + str(cu))
                    else:
                        contact = cl.getContact(msg.contentMetadata["mid"])
                        try:
                            cu = cl.channel.getCover(msg.contentMetadata["mid"])
                        except:
                            cu = ""
                        cl.sendText(msg.to,"[displayName]:\n" + contact.displayName + "\n[mid]:\n" + msg.contentMetadata["mid"] + "\n[statusMessage]:\n" + contact.statusMessage + "\n[pictureStatus]:\nhttp://dl.profile.line-cdn.net/" + contact.pictureStatus + "\n[coverURL]:\n" + str(cu))

            elif msg.text in ["Backup","backup"]:
                    try:
                        cl.updateDisplayPicture(backup.pictureStatus)
                        cl.updateProfile(backup)
                        cl.sendText(msg.to,"Backup done")
                    except Exception as e:
                        cl.sendText(msg.to, str (e))
            elif "Copy @" in msg.text:
               if msg.toType == 2:
                   print"[Copy]"
                   _name = msg.text.replace("Copy @","")
                   _nametarget = _name.rstrip(' ')
                   gs = cl.getGroup(msg.to)
                   targets=[]
                   for g in gs.members:
                       if _nametarget == g.displayName:
                          targets.append(g.mid)
                   if targets == []:
                       cl.sendText(msg.to,"Not Found")
                   else:
                       for target in targets:
                           try:
                               cl.CloneContactProfile(target)
                               cl.sendText(msg.to,"Success Copy")
                           except Exception as e:
                               print e 

            elif msg.contentType == 16:
                if wait["timeline"] == True:
                    msg.contentType = 0
                    if wait["lang"] == "JP":
                        msg.text = "menempatkan URL\n" + msg.contentMetadata["postEndUrl"]
                    else:
                        msg.text = "URLâ†’\n" + msg.contentMetadata["postEndUrl"]
                    cl.sendText(msg.to,msg.text)
            elif msg.text is None:
                return
            elif msg.text.lower() == 'help':
                if wait["lang"] == "JP":
                    cl.sendText(msg.to,helpMessage)
                else:
                    cl.sendText(msg.to,helpMessage)
            elif "Gn:" in msg.text:
                if msg.toType == 2:
                    group = cl.getGroup(msg.to)
                    group.name = msg.text.replace("Gn:","")
                    ki.updateGroup(group)
                else:
                    cl.sendText(msg.to,"Hal ini tidak dapat digunakan di luar kelompok👈")
            elif "Gn " in msg.text:
                if msg.toType == 2:
                    group = cl.getGroup(msg.to)
                    group.name = msg.text.replace("Gn ","")
                    cl.updateGroup(group)
                else:
                    cl.sendText(msg.to,"Can not be used for groups other than")
            elif "Kick:" in msg.text:
                midd = msg.text.replace("Kick:","")
                cl.kickoutFromGroup(msg.to,[midd])
            elif msg.text.lower() == 'invite':
                if msg.from_ in admin:
                  if msg.toType == 2:
                    wait["akaInvite"] = True
                    ki.sendText(msg.to,"send contact 😉")
            elif "Invite:" in msg.text:
                midd = msg.text.replace("Invite:","")
                cl.findAndAddContactsByMid(midd)
                cl.inviteIntoGroup(msg.to,[midd])
            elif "Mybot" == msg.text:
                msg.contentType = 13
                msg.contentMetadata = {'mid': kimid}
                cl.sendMessage(msg) 
                msg.contentType = 13
                msg.contentMetadata = {'mid': ki2mid}
                cl.sendMessage(msg) 
                msg.contentType = 13
                msg.contentMetadata = {'mid': ki3mid}
                cl.sendMessage(msg) 
                msg.contentType = 13
                msg.contentMetadata = {'mid': ki4mid}
                cl.sendMessage(msg)
                msg.contentType = 13
                msg.contentMetadata = {'mid': ki5mid}
                cl.sendMessage(msg) 
                msg.contentType = 13
                msg.contentMetadata = {'mid': ki6mid}
                cl.sendMessage(msg)
                msg.contentType = 13
                msg.contentMetadata = {'mid': ki7mid}
                cl.sendMessage(msg)
            elif "Me" == msg.text:
                msg.contentType = 13
                msg.contentMetadata = {'mid': mid}
                cl.sendMessage(msg)
            elif "S1" == msg.text:
                msg.contentType = 13
                msg.contentMetadata = {'mid': kimid}
                ki.sendMessage(msg)
            elif "S2" == msg.text:
                msg.contentType = 13
                msg.contentMetadata = {'mid': ki2mid}
                ki2.sendMessage(msg)
            elif "S3" == msg.text:
                msg.contentType = 13
                msg.contentMetadata = {'mid': ki3mid}
                ki3.sendMessage(msg)
            elif "S4" == msg.text:
                msg.contentType = 13
                msg.contentMetadata = {'mid': ki4mid}
                ki4.sendMessage(msg)
            elif "S5" == msg.text:
                msg.contentType = 13
                msg.contentMetadata = {'mid': ki5mid}
                ki5.sendMessage(msg)
            elif "S6" == msg.text:
                msg.contentType = 13
                msg.contentMetadata = {'mid': ki6mid}
                ki6.sendMessage(msg)
            elif "S7" == msg.text:
                msg.contentType = 13
                msg.contentMetadata = {'mid': ki7mid}
                ki7.sendMessage(msg)
            elif msg.text.lower() == 'Hore':
                msg.contentType = 7
                msg.text = None
                msg.contentMetadata = {
                                     "STKID": "16846756",
                                     "STKPKGID": "8543",
                                     "STKVER": "7" }
                cl.sendMessage(msg)
                cl.sendMessage(msg)
                cl.sendMessage(msg)
            elif msg.text.lower() == 'Ok':
                msg.contentType = 7
                msg.text = None
                msg.contentMetadata = {
                                     "STKID": "16846755",
                                     "STKPKGID": "8543",
                                     "STKVER": "7" }
                cl.sendMessage(msg)
                cl.sendMessage(msg)
                cl.sendMessage(msg)
            elif msg.text.lower() == 'Siap bos':
                msg.contentType = 7
                msg.text = None
                msg.contentMetadata = {
                                     "STKID": "16846757",
                                     "STKPKGID": "8543",
                                     "STKVER": "7" }
                cl.sendMessage(msg)
                cl.sendMessage(msg)
                cl.sendMessage(msg)
            elif msg.text.lower() == 'Thanks':
                msg.contentType = 7
                msg.text = None
                msg.contentMetadata = {
                                     "STKID": "16846759",
                                     "STKPKGID": "8543",
                                     "STKVER": "7" }
                cl.sendMessage(msg)
                cl.sendMessage(msg)
                cl.sendMessage(msg)
            elif msg.text.lower() == 'Lol':
                msg.contentType = 7
                msg.text = None
                msg.contentMetadata = {
                                     "STKID": "16846776",
                                     "STKPKGID": "8543",
                                     "STKVER": "7" }
                cl.sendMessage(msg)
                cl.sendMessage(msg)
                cl.sendMessage(msg)
            elif msg.text.lower() == 'Sue':
                msg.contentType = 7
                msg.text = None
                msg.contentMetadata = {
                                     "STKID": "16846777",
                                     "STKPKGID": "8543",
                                     "STKVER": "7" }
                cl.sendMessage(msg)
                cl.sendMessage(msg)
                cl.sendMessage(msg)
            elif msg.text.lower() == 'No':
                msg.contentType = 7
                msg.text = None
                msg.contentMetadata = {
                                     "STKID": "16846777",
                                     "STKPKGID": "8543",
                                     "STKVER": "7" }
                cl.sendMessage(msg)
                cl.sendMessage(msg)
                cl.sendMessage(msg)
            elif msg.text.lower() == 'Suntuk':
                msg.contentType = 7
                msg.text = None
                msg.contentMetadata = {
                                     "STKID": "14875040",
                                     "STKPKGID": "1380280",
                                     "STKVER": "1" }
                cl.sendMessage(msg)
                cl.sendMessage(msg)
                cl.sendMessage(msg)
            elif msg.text.lower() == 'Apa':
                msg.contentType = 7
                msg.text = None
                msg.contentMetadata = {
                                     "STKID": "14875046",
                                     "STKPKGID": "1380280",
                                     "STKVER": "1" }
                cl.sendMessage(msg)
                cl.sendMessage(msg)
                cl.sendMessage(msg)
            elif msg.text.lower() == '?':
                msg.contentType = 7
                msg.text = None
                msg.contentMetadata = {
                                     "STKID": "14875046",
                                     "STKPKGID": "1380280",
                                     "STKVER": "1" }
                cl.sendMessage(msg)
                cl.sendMessage(msg)
                cl.sendMessage(msg)
            elif msg.text.lower() == 'Pose dulu':
                msg.contentType = 7
                msg.text = None
                msg.contentMetadata = {
                                     "STKID": "14875030",
                                     "STKPKGID": "1380280",
                                     "STKVER": "1" }
                cl.sendMessage(msg)
                cl.sendMessage(msg)
                cl.sendMessage(msg)
            elif msg.text.lower() == '250c':
                msg.contentType = 9
                msg.contentMetadata={'PRDTYPE': 'STICKER',
                                    'STKVER': '1',
                                    'MSGTPL': '5',
                                    'STKPKGID': '1380280'}
                msg.text = None
                cl.sendMessage(msg)
            elif msg.text.lower() == '200c':
                msg.contentType = 9
                msg.contentMetadata={'PRDTYPE': 'STICKER',
                                    'STKVER': '1',
                                    'MSGTPL': '5',
                                    'STKPKGID': '1319678'}
                msg.text = None
                cl.sendMessage(msg)
            elif msg.text.lower() == 'Njiir':
                msg.contentType = 9
                msg.contentMetadata={'PRDTYPE': 'STICKER',
                                    'STKVER': '1',
                                    'MSGTPL': '5',
                                    'STKPKGID': '1300191'}
                msg.text = None
                cl.sendMessage(msg)
            elif msg.text.lower() == 'Hadiah':
                msg.contentType = 9
                msg.contentMetadata={'PRDTYPE': 'STICKER',
                                    'STKVER': '1',
                                    'MSGTPL': '5',
                                    'STKPKGID': '5033'}
                msg.text = None
                cl.sendMessage(msg)

                ki6.sendMessage(msg)
            elif msg.text in ["Gift","gift"]:
                msg.contentType = 9
                msg.contentMetadata={'PRDID': '3b92ccf5-54d3-4765-848f-c9ffdc1da020',
                                    'PRDTYPE': 'THEME',
                                    'MSGTPL': '2'}
                msg.text = None
                cl.sendMessage(msg)
            elif msg.text in ["Gift you","All gift"]:
                msg.contentType = 9
                msg.contentMetadata={'PRDID': '3b92ccf5-54d3-4765-848f-c9ffdc1da020',
                                    'PRDTYPE': 'THEME',
                                    'MSGTPL': '3'}
                msg.text = None
                cl.sendMessage(msg)
                ki.sendMessage(msg)
                ki2.sendMessage(msg)
                ki3.sendMessage(msg)
                ki4.sendMessage(msg)
                ki5.sendMessage(msg)
                ki6.sendMessage(msg)
                ki7.sendMessage(msg)
            elif msg.text in ["Bot2 Gift","Bot2 gift"]:
                msg.contentType = 9
                msg.contentMetadata={'PRDID': '3b92ccf5-54d3-4765-848f-c9ffdc1da020',
                                    'PRDTYPE': 'THEME',
                                    'MSGTPL': '3'}
                msg.text = None
                ki2.sendMessage(msg)
            elif msg.text in ["Bot3 Gift","Bot3 gift"]:
                msg.contentType = 9
                msg.contentMetadata={'PRDID': '3b92ccf5-54d3-4765-848f-c9ffdc1da020',
                                    'PRDTYPE': 'THEME',
                                    'MSGTPL': '4'}
                msg.text = None
                ki3.sendMessage(msg)
            elif msg.text in ["Bot1 Gift","Bot1 gift"]:
                msg.contentType = 9
                msg.contentMetadata={'PRDID': '3b92ccf5-54d3-4765-848f-c9ffdc1da020',
                                    'PRDTYPE': 'THEME',
                                    'MSGTPL': '5'}
                msg.text = None
                ki.sendMessage(msg)     
            elif msg.text in ["Cury PP"]:
                if msg.from_ in admin:
                    tl_text = msg.text.replace("TL","")
                    cl.sendText(msg.to,"line://home/post?userMid="+mid+"&postId="+cl.new_post(tl_text)["result"]["post"]["postInfo"]["postId"])
            elif msg.text in ["BCancel"]:
                if msg.toType == 2:
                    group = ki.getGroup(msg.to)
                    if group.invitee is not None:
                        gInviMids = [contact.mid for contact in group.invitee]
                        ki.cancelGroupInvitation(msg.to, gInviMids)
                    else:
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,"No invites👈")
                        else:
                            cl.sendText(msg.to,"Invite people inside not👈")
                else:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Tidak ada undangan")
                    else:
                        cl.sendText(msg.to,"invitan tidak ada")

            elif msg.text in ["Batal"]:
                if msg.toType == 2:
                    group = cl.getGroup(msg.to)
                    if group.invitee is not None:
                        gInviMids = [contact.mid for contact in group.invitee]
                        cl.cancelGroupInvitation(msg.to, gInviMids)
                    else:
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,"No invites👈")
                        else:
                            cl.sendText(msg.to,"Invite people inside not👈")
                else:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Tidak ada undangan👈")
                    else:
                        cl.sendText(msg.to,"invitan tidak ada")
                                               
            elif "Comment set:" in msg.text:
                c = msg.text.replace("Comment set:","")
                if c in [""," ","\n",None]:
                    cl.sendText(msg.to,"Error")
                else:
                    wait["comment"] = c
                    cl.sendText(msg.to,"It was changed。\n\n" + c)
            elif msg.text in ["Comment check"]:
                 cl.sendText(msg.to,"An automatic comment is established as follows at present。\n\n" + str(wait["comment"]))
            elif msg.text in ["コメント:オン","Comment:on"]:
                if wait["commentOn"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Done。")
                else:
                    wait["commentOn"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Already。")
            elif msg.text in ["コメント:オフ","Comment:off"]:
                if wait["commentOn"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Done。")
                else:
                    wait["commentOn"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Already。")                        
            #elif "gurl" == msg.text:
                #print cl.getGroup(msg.to)
                ##cl.sendMessage(msg)
            elif msg.text in ["Link on"]:
                if msg.toType == 2:
                    group = cl.getGroup(msg.to)
                    group.preventJoinByTicket = False
                    cl.updateGroup(group)
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"URL open ô€¨ô€„Œ")
                    else:
                        cl.sendText(msg.to,"URL open ô€¨ô€„Œ")
                else:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"It can not be used outside the group ô€œô€„‰👈")
                    else:
                        cl.sendText(msg.to,"Can not be used for groups other than ô€œô€„‰")
            elif msg.text in ["Link off"]:
                if msg.toType == 2:
                    group = cl.getGroup(msg.to)
                    group.preventJoinByTicket = True
                    cl.updateGroup(group)
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"URL close ô€¨👈")
                    else:
                        cl.sendText(msg.to,"URL close ô€¨👈")
                else:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"It can not be used outside the group  👈")
                    else:
                        cl.sendText(msg.to,"Can not be used for groups other than ô€œ")
                        
            elif "Tiket " in msg.text.lower():
                rplace=msg.text.lower().replace("Tiket ")
                if rplace == "on":
                        wait["atjointicket"]=True
                elif rplace == "off":
                        wait["atjointicket"]=False
                cl.sendText(msg.to,"Auto Join Group by Ticket is %s" % str(wait["atjointicket"]))
            elif '/ti/g/' in msg.text.lower():
                link_re = re.compile('(?:line\:\/|line\.me\/R)\/ti\/g\/([a-zA-Z0-9_-]+)?')
                links = link_re.findall(msg.text)
                n_links=[]
                for l in links:
                        if l not in n_links:
                                n_links.append(l)
                for ticket_id in n_links:
                        if wait["atjointicket"] == True:
                                group=cl.findGroupByTicket(ticket_id)
                                cl.acceptGroupInvitationByTicket(group.id,ticket_id)
                                cl.sendText(msg.to,"Sukses join ke grup %s" % str(group.name))  

            elif msg.text.lower() == "Invite:gcreator":
                if msg.toType == 2:
                       ginfo = cl.getGroup(msg.to)
                       try:
                           gcmid = ginfo.creator.mid
                       except:
                           gcmid = "Error"
                       if wait["lang"] == "JP":
                           cl.inviteIntoGroup(msg.to,[gcmid])
                       else:
                           cl.inviteIntoGroup(msg.to,[gcmid])
            elif msg.text.lower() == 'Bot:gcreator':
                if msg.toType == 2:
                       ginfo = ki.getGroup(msg.to)
                       try:
                           gcmid = ginfo.creator.mid
                       except:
                           gcmid = "Error"
                       if wait["lang"] == "JP":
                           ki.inviteIntoGroup(msg.to,[gcmid])
                       else:
                           ki.inviteIntoGroup(msg.to,[gcmid])

            elif msg.text == "Ginfo":
                if msg.toType == 2:
                    ginfo = cl.getGroup(msg.to)
                    try:
                        gCreator = ginfo.creator.displayName
                    except:
                        gCreator = "Error"
                    if wait["lang"] == "JP":
                        if ginfo.invitee is None:
                            sinvitee = "0"
                        else:
                            sinvitee = str(len(ginfo.invitee))
                        if ginfo.preventJoinByTicket == True:
                            u = "close"
                        else:
                            u = "open"
                msg.contentType = 13
                msg.contentMetadata = {'mid': ginfo.creator.mid}                          
                cl.sendText(msg.to,"「 ID 」\nGroup Name:\n" + str(ginfo.name) + "\n\nGroup ID:\n" + msg.to + "\n\nGroup Creator:\n" + gCreator + "\n\nProfile status:\nhttp://dl.profile.line.naver.jp/" + ginfo.pictureStatus + "\n\nmembers:" + str(len(ginfo.members)) + " members\npending:" + sinvitee + " people\nURL:" + u + "it is inside")
                cl.sendMessage(msg)
            elif "Contact" == msg.text:
                msg.contentType = 13
                msg.contentMetadata = {'mid': msg.to}
                cl.sendMessage(msg)
            elif "Gcreator" == msg.text:
              if msg.toType == 2:
                    ginfo = cl.getGroup(msg.to)
                    try:
                        gCreator = ginfo.creator.displayName
                    except:
                        gCreator = "Error"
                    cl.sendText(msg.to, "Group Creator : " + gCreator)
            elif msg.text in ["Creator"]:
                    msg.contentType = 13
                    msg.contentMetadata = {'mid': "ucbd1374cb68242824dc21abcd7d6f669"}
                    cl.sendText(msg.to,"〘MyCreator〙")
                    ki.sendText(msg.to,"Jangan Lupa Di Add Ya!!!")
                    ki1.sendMessage(msg)
                    msg.contentType = 13
                    msg.contentMetadata = {'mid': "u3fa0c0964985cd663d1fce84507e9b9b"}
                    ki2.sendText(msg.to,"〘MyCreator〙")
                    ki3.sendText(msg.to,"Jangan Lupa Di Add Ya!!!")
                    ki4.sendMessage(msg)
                        
                    except:
                        Creatorbot = "Error"
                    ki5.sendText(msg.to, "Owner: =>> http://line.me/ti/p/~rd.rmdhn")
                    ki6.sendMessage(msg)

            elif msg.text.lower() == "Glist":
                gs = cl.getGroupIdsJoined()
                num=1
                L = "☫『 Groups-⚚-List 』☫\n"
                for i in gs:
                    L += "\n%i. %s\n%s\n" % (num, cl.getGroup(i).name + " | " + str(len (cl.getGroup(i).members)), i)
                    num=(num+1)
                L += "\n\n☫ Total Groups : [ %i ]" % len(gs)
                cl.sendText(msg.to, L + "\n\n                   °✍☬⟿SERK TEAM⟿☬̢ ") 
            elif msg.text in ["List group"]:
                if msg.from_ in admin:
                    gid = cl.getGroupIdsJoined()
                    h = ""
                    for i in gid:
                        h += "[~]%s\n" % (cl.getGroup(i).name   +str (len (cl.getGroup(i).members)))
                    cl.sendText(msg.to,"========[List Group]========\n"+ h +"Total Group :" +str(len(gid)))
            elif "Memid" == msg.text:
                cl.sendText(msg.to,mid)
            elif "All mid" == msg.text:
                ki.sendText(msg.to,kimid)
                ki2sendText(msg.to,ki2mid)
                ki3.sendText(msg.to,ki3mid)
                ki4.sendText(msg.to,ki4mid)
                ki5.sendText(msg.to,ki5mid)
                ki6.sendText(msg.to,ki6mid)
            elif "Mybot mid" == msg.text:
                msg.contentType = 13
                msg.contentMetadata = {'mid': kimid}
                cl.sendMessage(msg)
                msg.contentType = 13
                msg.contentMetadata = {'mid': ki2mid}
                cl.sendMessage(msg)
                msg.contentType = 13
                msg.contentMetadata = {'mid': ki3mid}
                cl.sendMessage(msg)
                msg.contentType = 13
                msg.contentMetadata = {'mid': ki4mid}
                cl.sendMessage(msg)
                msg.contentType = 13
                msg.contentMetadata = {'mid': ki5mid}
                cl.sendMessage(msg)
                msg.contentType = 13
                msg.contentMetadata = {'mid': ki6mid}
                cl.sendMessage(msg)
                msg.contentType = 13
                msg.contentMetadata = {'mid': ki7mid}
                cl.sendMessage(msg)
            elif msg.text in ["Test"]:
                if msg.from_ in admin:
                    cl.sendText(msg.to,"Serk1 HADIR҉̸ ")
                    ki.sendText(msg.to,"Serk2 HADIR҉̸ ")
                    ki2.sendText(msg.to,"Serk3 HADIR҉̸ ")
                    ki3.sendText(msg.to,"Serk4 HADIR҉̸ ")    
                    ki4.sendText(msg.to,"Serk5 HADIR҉̸ ")
                    ki5.sendText(msg.to,"Serk6 HADIR҉̸ ")
                    ki6.sendText(msg.to,"Serk6 HADIR҉̸ ")
                    ki7.sendText(msg.to,"Serk6 HADIR҉̸ ")
            elif "TL: " in msg.text:
                tl_text = msg.text.replace("TL: ","")
                cl.sendText(msg.to,"line://home/post?userMid="+mid+"&amp;postId="+cl.new_post(tl_text)["result"]["post"]["postInfo"]["postId"])
            elif "All: " in msg.text:
                string = msg.text.replace("All: ","")
                if len(string.decode('utf-8')) <= 20:
                    profile = ki.getProfile()
                    profile.displayName = string
                    ki.updateProfile(profile)
                if len(string.decode('utf-8')) <= 20:
                    profile = ki2.getProfile()
                    profile.displayName = string
                    ki2.updateProfile(profile)
                if len(string.decode('utf-8')) <= 20:
                    profile = ki3.getProfile()
                    profile.displayName = string
                    ki3.updateProfile(profile)
                if len(string.decode('utf-8')) <= 20:
                    profile = ki4.getProfile()
                    profile.displayName = string
                    ki4.updateProfile(profile)
                if len(string.decode('utf-8')) <= 20:
                    profile = ki5.getProfile()
                    profile.displayName = string
                    ki5.updateProfile(profile)
                if len(string.decode('utf-8')) <= 20:
                    profile = ki6.getProfile()
                    profile.displayName = string
                    ki6.updateProfile(profile)
            elif "Mybio: " in msg.text:
                string = msg.text.replace("Mybio: ","")
                if len(string.decode('utf-8')) <= 500:
                    profile = cl.getProfile()
                    profile.statusMessage = string
                    cl.updateProfile(profile)
                    cl.sendText(msg.to,"􀜁􀇔􏿿Update Bio👉" + string + "👈")
            elif "Allbio: " in msg.text:
                string = msg.text.replace("Allbio: ","")
                if len(string.decode('utf-8')) <= 500:
                    profile = ki.getProfile()
                    profile.statusMessage = string
                    ki.updateProfile(profile)
                if len(string.decode('utf-8')) <= 500:
                    profile = ki2.getProfile()
                    profile.statusMessage = string
                    ki2.updateProfile(profile)
                if len(string.decode('utf-8')) <= 500:
                    profile = ki3.getProfile()
                    profile.statusMessage = string
                    ki3.updateProfile(profile)
                if len(string.decode('utf-8')) <= 500:
                    profile = ki4.getProfile()
                    profile.statusMessage = string
                    ki4.updateProfile(profile)
                if len(string.decode('utf-8')) <= 500:
                    profile = ki5.getProfile()
                    profile.statusMessage = string
                    ki5.updateProfile(profile)
                if len(string.decode('utf-8')) <= 500:
                    profile = ki6.getProfile()
                    profile.statusMessage = string
                    ki6.updateProfile(profile)
            elif "Myname:" in msg.text:
                string = msg.text.replace("Myname:","")
                if len(string.decode('utf-8')) <= 20:
                    profile = cl.getProfile()
                    profile.displayName = string
                    cl.updateProfile(profile)
                    cl.sendText(msg.to,"􀜁􀇔􏿿Update Names👉 " + string + "👈")
#---------------------------------------------------------
            elif "S1name:" in msg.text:
                string = msg.text.replace("S1name:","")
                if len(string.decode('utf-8')) <= 20:
                    profile = ki.getProfile()
                    profile.displayName = string
                    ki.updateProfile(profile)
                    ki.sendText(msg.to,"􀜁􀇔􏿿Update Names👉" + string + "👈")
#--------------------------------------------------------
            elif "S2name:" in msg.text:
                string = msg.text.replace("S2name:","")
                if len(string.decode('utf-8')) <= 20:
                    profile = ki2.getProfile()
                    profile.displayName = string
                    ki2.updateProfile(profile)
                    ki2.sendText(msg.to,"􀜁􀇔􏿿Update Names👉" + string + "👈")
#--------------------------------------------------------
            elif "S3name:" in msg.text:
                string = msg.text.replace("S3name:","")
                if len(string.decode('utf-8')) <= 20:
                    profile = ki3.getProfile()
                    profile.displayName = string
                    ki3.updateProfile(profile)
                    ki3.sendText(msg.to,"􀜁􀇔􏿿Update Names👉" + string + "👈")
#--------------------------------------------------------
            elif "S4name:" in msg.text:
                string = msg.text.replace("S4name:","")
                if len(string.decode('utf-8')) <= 20:
                    profile = ki4.getProfile()
                    profile.displayName = string
                    ki4.updateProfile(profile)
                    ki4.sendText(msg.to,"􀜁􀇔􏿿Update Names👉" + string + "👈")
#--------------------------------------------------------
            elif "S5name:" in msg.text:
                string = msg.text.replace("S5name:","")
                if len(string.decode('utf-8')) <= 20:
                    profile = ki5.getProfile()
                    profile.displayName = string
                    ki5.updateProfile(profile)
                    ki5.sendText(msg.to,"􀜁􀇔􏿿Update Names👉" + string + "👈")
#--------------------------------------------------------
            elif "S6name:" in msg.text:
                string = msg.text.replace("S6name:","")
                if len(string.decode('utf-8')) <= 20:
                    profile = ki6.getProfile()
                    profile.displayName = string
                    ki6.updateProfile(profile)
                    ki6.sendText(msg.to,"􀜁􀇔􏿿Update Names👉" + string + "👈")
#--------------------------------------------------------
            elif "S7name:" in msg.text:
                string = msg.text.replace("S7name:","")
                if len(string.decode('utf-8')) <= 20:
                    profile = ki7.getProfile()
                    profile.displayName = string
                    ki7.updateProfile(profile)
                    ki7.sendText(msg.to,"􀜁􀇔􏿿Update Names👉" + string + "👈")
#--------------------------------------------------------
            elif "Mc " in msg.text:
                key = eval(msg.contentMetadata["MENTION"])
                key1 = key["MENTIONEES"][0]["M"]
                cl.sendText(msg.to,"Mc: " + key1)
            elif "Mc: " in msg.text:
                mmid = msg.text.replace("Mc: ","")
                msg.contentType = 13
                msg.contentMetadata = {"mid":mmid}
                cl.sendMessage(msg)
            elif "Mid:" in msg.text:
                mmid = msg.text.replace("Mid:","")
                msg.contentType = 13
                msg.contentMetadata = {"mid":mmid}
                cl.sendMessage(msg)
            elif msg.text.lower() == 'contact on':
                if wait["contact"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Sudah On")
                    else:
                        cl.sendText(msg.to,"It is already open")
                else:
                    wait["contact"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"already open 👈")
                    else:
                        cl.sendText(msg.to,"It is already open 􀜁􀇔􏿿")
            elif msg.text.lower() == 'contact off':
                if wait["contact"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"sudah off ô€œô€„‰👈")
                    else:
                        cl.sendText(msg.to,"It is already off ô€œô€„‰👈")
                else:
                    wait["contact"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"off ô€œô€„‰already")
                    else:
                        cl.sendText(msg.to,"already Close ô€œô€„‰👈")
            elif msg.text.lower() == 'protectall on':
                if wait["protect"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Ini sudah on 􀜁􀇔􏿿👈")
                    else:
                        cl.sendText(msg.to,"Hal ini sudah terbuka ô€¨👈")
                else:
                    wait["protect"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"already ON􀜁􀇔􏿿")
                    else:
                        cl.sendText(msg.to,"It is already On ô€¨")
                if wait["linkprotect"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Ini sudah on 􀜁􀇔􏿿👈")
                    else:
                        cl.sendText(msg.to,"Hal ini sudah terbuka ô€¨👈")
                else:
                    wait["linkprotect"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"already ON􀜁􀇔􏿿")
                    else:
                        cl.sendText(msg.to,"It is already On ô€¨")
                if wait["inviteprotect"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Ini sudah on 􀜁􀇔􏿿👈")
                    else:
                        cl.sendText(msg.to,"Hal ini sudah terbuka ô€¨👈")
                else:
                    wait["inviteprotect"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"already ON􀜁􀇔􏿿")
                    else:
                        cl.sendText(msg.to,"It is already On ô€¨")
                if wait["cancelprotect"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Ini sudah on 􀜁􀇔􏿿👈")
                    else:
                        cl.sendText(msg.to,"Hal ini sudah terbuka ô€¨👈")
                else:
                    wait["calncelprotect"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"already ON􀜁􀇔􏿿")
                    else:
                        cl.sendText(msg.to,"It is already On ô€¨")
           # elif msg.text.lower() == 'protect on':
                if wait["protect"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Ini sudah on 􀜁??􏿿👈")
                    else:
                        cl.sendText(msg.to,"Hal ini sudah terbuka ô€¨👈")
                else:
                    wait["protect"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"already ON􀜁􀇔􏿿")
                    else:
                        cl.sendText(msg.to,"It is already On ô€¨")
            elif msg.text.lower() == 'qrprotect on':
                if wait["linkprotect"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Ini sudah on 􀜁􀇔􏿿👈")
                    else:
                        cl.sendText(msg.to,"Hal ini sudah terbuka ô€¨👈")
                else:
                    wait["linkprotect"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"already ON􀜁􀇔􏿿")
                    else:
                        cl.sendText(msg.to,"It is already On ô€¨")
            elif msg.text.lower() == 'inviteprotect on':
                if wait["inviteprotect"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Ini sudah on 􀜁􀇔􏿿👈")
                    else:
                        cl.sendText(msg.to,"Hal ini sudah terbuka ô€¨👈")
                else:
                    wait["inviteprotect"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"already ON􀜁􀇔􏿿")
                    else:
                        cl.sendText(msg.to,"It is already On ô€¨")
            elif msg.text.lower() == 'cancelprotect on':
                if wait["cancelprotect"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Ini sudah on 􀜁􀇔􏿿👈")
                    else:
                        cl.sendText(msg.to,"Hal ini sudah terbuka ô€¨👈")
                else:
                    wait["cancelprotect"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"already ON􀜁􀇔􏿿")
                    else:
                        cl.sendText(msg.to,"It is already On ô€¨")
            elif msg.text.lower() == 'auto join on':
                if wait["autoJoin"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Ini sudah off 􀜁􀇔􏿿👈")
                    else:
                        cl.sendText(msg.to,"Hal ini sudah terbuka ô€¨👈")
                else:
                    wait["autoJoin"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"already ON􀜁􀇔􏿿")
                    else:
                        cl.sendText(msg.to,"It is already On ô€¨")
            elif msg.text.lower() == 'blocklist':
                blockedlist = cl.getBlockedContactIds()
                cl.sendText(msg.to, "Please wait...")
                kontak = cl.getContacts(blockedlist)
                num=1
                msgs="User Blocked List\n"
                for ids in kontak:
                    msgs+="\n%i. %s" % (num, ids.displayName)
                    num=(num+1)
                msgs+="\n\nTotal %i blocked user(s)" % len(kontak)
                cl.sendText(msg.to, msgs)
            elif msg.text.lower() == 'auto join off':
                if wait["autoJoin"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Auto Join Already Off")
                    else:
                        cl.sendText(msg.to,"Auto Join set off")
                else:
                    wait["autoJoin"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"already close")
                    else:
                        cl.sendText(msg.to,"It is already open ô€œ👈") 
            elif msg.text in ["Protectall off","Proall off"]:
                if wait["protect"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"hall ini sudah off ô€œ👈")
                    else:
                        cl.sendText(msg.to,"sudah dimatikan ô€œô€„‰👈")
                else:
                    wait["protect"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"already close")
                    else:
                        cl.sendText(msg.to,"It is already open ô€œ👈")
                if wait["linkprotect"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"hall ini sudah off ô€œ👈")
                    else:
                        cl.sendText(msg.to,"sudah dimatikan ô€œô€„‰👈")
                else:
                    wait["linkprotect"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"already close")
                    else:
                        cl.sendText(msg.to,"It is already open ô€œ👈")
                if wait["inviteprotect"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"hall ini sudah off ô€œ👈")
                    else:
                        cl.sendText(msg.to,"sudah dimatikan ô€œô€„‰👈")
                else:
                    wait["inviteprotect"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"already close")
                    else:
                        cl.sendText(msg.to,"It is already open ô€œ👈")
                if wait["cancelprotect"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"hall ini sudah off ô€œ👈")
                    else:
                        cl.sendText(msg.to,"sudah dimatikan ô€œô€„‰👈")
                else:
                    wait["cancelprotect"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"already close")
                    else:
                        cl.sendText(msg.to,"It is already open ô€œ👈")
            #elif msg.text in ["Protect off","Pro off"]:
                if wait["protect"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"hall ini sudah off ô€œ👈")
                    else:
                        cl.sendText(msg.to,"sudah dimatikan ô€œô€„‰👈")
                else:
                    wait["protect"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"already close")
                    else:
                        cl.sendText(msg.to,"It is already open ô€œ👈")
            elif msg.text in ["Qrprotect off","Qr off"]:
                if wait["linkprotect"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"hall ini sudah off ô€œ👈")
                    else:
                        cl.sendText(msg.to,"sudah dimatikan ô€œô€„‰👈")
                else:
                    wait["linkprotect"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"already close")
                    else:
                        cl.sendText(msg.to,"It is already open ô€œ👈")
            elif msg.text in ["Inviteprotect off","Invite off"]:
                if wait["inviteprotect"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"hall ini sudah off ô€œ👈")
                    else:
                        cl.sendText(msg.to,"sudah dimatikan ô€œô€„‰👈")
                else:
                    wait["inviteprotect"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"already close")
                    else:
                        cl.sendText(msg.to,"It is already open ô€œ👈")
            elif msg.text in ["Cancelprotect off","Cancel off"]:
                if wait["cancelprotect"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"hall ini sudah off ô€œ👈")
                    else:
                        cl.sendText(msg.to,"sudah dimatikan ô€œô€„‰👈")
                else:
                    wait["cancelprotect"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"already close")
                    else:
                        cl.sendText(msg.to,"It is already open ô€œ👈")
            elif "Gcancel:" in msg.text:
                try:
                    strnum = msg.text.replace("Gcancel:","")
                    if strnum == "off":
                        wait["autoCancel"]["on"] = False
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,"Itu off undangan ditolak👈\nSilakan kirim dengan menentukan jumlah orang ketika Anda menghidupkan👈")
                        else:
                            cl.sendText(msg.to,"Off undangan ditolak👈Sebutkan jumlah terbuka ketika Anda ingin mengirim")
                    else:
                        num =  int(strnum)
                        wait["autoCancel"]["on"] = True
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,strnum + "Kelompok berikut yang diundang akan ditolak secara otomatis👈")
                        else:
                            cl.sendText(msg.to,strnum + "The team declined to create the following automatic invitation")
                except:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Nilai tidak benar👈")
                    else:
                        cl.sendText(msg.to,"Weird value🛡")
            elif msg.text in ["Auto leave on","Leave on"]:
                if wait["leaveRoom"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"on👈􀜁􀇔􏿿")
                    else:
                        cl.sendText(msg.to,"Sudah terbuka 􀜁􀇔􏿿")
                else:
                    wait["leaveRoom"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Done👈􀜁􀇔􏿿")
                    else:
                        cl.sendText(msg.to,"Is already open👈􀜁􀇔􏿿")
            elif msg.text in ["Auto leave off","Leave off"]:
                if wait["leaveRoom"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"on👈􀜁􀇔􏿿")
                    else:
                        cl.sendText(msg.to,"Sudah off👈􀜁􀇔􏿿")
                else:
                    wait["leaveRoom"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Done👈􀜁􀇔􏿿")
                    else:
                        cl.sendText(msg.to,"Is already close👈􀜁􀇔􏿿")
            elif msg.text in ["Share on","K on"]:
                if wait["timeline"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Done 􀜁􀇔􏿿")
                    else:
                        cl.sendText(msg.to,"Hal ini sudah terbuka👈")
                else:
                    wait["timeline"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"on👈")
                    else:
                        cl.sendText(msg.to,"on👈")
            elif msg.text in ["Share off","K off"]:
                if wait["timeline"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Done👈􀜁􀇔􏿿")
                    else:
                        cl.sendText(msg.to,"It is already turned off 􀜁􀇔􏿿👈")
                else:
                    wait["timeline"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Off👈")
                    else:
                        cl.sendText(msg.to,"Off👈")
#--------------------------------------------------------
            elif "Group pict" in msg.text.lower():            
                print "[command]steal executing"
                group = cl.getGroup(msg.to)
                path = "http://dl.profile.line-cdn.net/" + group.pictureStatus
                cl.sendImageWithURL(msg.to,path)
                print "[command]steal executed"
#--------------------------------------------------------
            elif msg.text.lower() == 'Set':
                md = "✃┈┈☫ รεƭƭเɳɠร ☫┈┈✍ \n\n"
                if wait["contact"] == True: md+=" ❂͜͡☆➣ Contact:on \n"
                else: md+=" ❂͜͡☆➣Contact:off􀜁􀄰 \n"
                if wait["autoJoin"] == True: md+=" ❂͜͡☆➣ Auto Join:on \n"
                else: md +=" ❂͜͡☆➣ Auto Join:off \n"
                if wait["autoCancel"]["on"] == True:md+=" ❂͜͡☆➣ Auto cancel:" + str(wait["autoCancel"]["members"]) + " \n"
                else: md+=" ❂͜͡☆➣ Group cancel:off \n"
                if wait["likeOn"] == True: md+=" ❂͜͡☆➣ Auto Like:on \n"
                else: md+=" ❂͜͡☆➣ Auto Like:off \n"
                if wait["leaveRoom"] == True: md+=" ❂͜͡☆➣ Auto leave:on \n"
                else: md+=" ❂͜͡☆➣ Auto leave:off \n"
                if wait["timeline"] == True: md+=" ❂͜͡☆➣ Share:on \n"
                else:md+=" ❂͜͡☆➣ Share:off \n"
                if wait["autoAdd"] == True: md+=" ❂͜͡☆➣ Auto add:on \n"
                else:md+=" ❂͜͡☆➣ Auto add:off \n"
                if wait["Backup"] == True: md+=" ❂͜͡☆➣ Backup:on \n"
                else:md+=" ❂͜͡☆➣ Backup:off \n"
                if wait["commentOn"] == True: md+=" ❂͜͡☆➣ Auto Coment:on \n"
                else:md+=" ❂͜͡☆➣ Auto Coment:off \n"
                if wait["protect"] == True: md+=" ❂͜͡☆➣ Protect:on \n"
                else:md+=" ❂͜͡☆➣Protect:off \n"
                if wait["linkprotect"] == True: md+=" ❂͜͡☆➣ ProtectQr:on \n"
                else:md+=" ❂͜͡☆➣ PotectQr:off \n"
                if wait["inviteprotect"] == True: md+=" ❂͜͡☆➣ Invite Protect:on \n"
                else:md+=" ❂͜͡☆➣ Invite Protect:off \n"
                if wait["MProtection"] == True: md+=" ❂͜͡☆➣ MProtection:on \n"
                else: md+=" ❂͜͡☆➣ MProtection:off \n"
                if wait["cancelprotect"] == True: md+=" ❂͜͡☆➣ Cancel Protect:on \n"
                else:md+=" ❂͜͡☆➣ Cancel Protect:off \n"
                if wait["atjointicket"] == True: md+=" ❂͜͡☆➣ AtJoin Group Ticket:on \n"
                else:md+=" ❂͜͡☆➣ Atjoin Group Ticket:off \n\n ☬⟿ℛℹℴ⟿Ȿ⟿ℬᝪᝨ⟿☬"
                cl.sendText(msg.to,md)
                msg.contentType = 13
                msg.contentMetadata = {'Mid': admsa}
                cl.sendMessage(msg)
            elif msg.text.lower() == 'Me':
                msg.contentType = 13
                msg.contentMetadata = {'mid': mid}
                cl.sendMessage(msg)
            elif cms(msg.text,["creator","Mee"]):
                msg.contentType = 13
                msg.contentMetadata = {'mid': admsa}
                cl.sendText(msg.to,"down􏿿􂤁􀆋down􏿿􂤁􀆋down􏿿􂤁􀆋down􏿿􂤁􀆋down􏿿􂤁􀆋down􏿿􂤁􀆋down􏿿")
                cl.sendMessage(msg)
                cl.sendText(msg.to,"up􏿿􂤁􀆊up􏿿􂤁􀆊up􏿿􂤁􀆊upupupup")            
            elif "Set album:" in msg.text:
                gid = msg.text.replace("Set album:","")
                album = cl.getAlbum(gid)
                if album["result"]["items"] == []:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Tidak ada album👈")
                    else:
                        cl.sendText(msg.to,"Dalam album tidak👈")
                else:
                    if wait["lang"] == "JP":
                        mg = "Berikut ini adalah album dari target"
                    else:
                        mg = "Berikut ini adalah subjek dari album"
                    for y in album["result"]["items"]:
                        if "photoCount" in y:
                            mg += str(y["title"]) + ":" + str(y["photoCount"]) + "æžš\n"
                        else:
                            mg += str(y["title"]) + ":0 Pieces\n"
                    cl.sendText(msg.to,mg)
            elif "Album " in msg.text:
                gid = msg.text.replace("Album ","")
                album = cl.getAlbum(gid)
                if album["result"]["items"] == []:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Tidak ada album")
                    else:
                        cl.sendText(msg.to,"Dalam album tidak")
                else:
                    if wait["lang"] == "JP":
                        mg = "Berikut ini adalah album dari target"
                    else:
                        mg = "Berikut ini adalah subjek dari album"
                    for y in album["result"]["items"]:
                        if "photoCount" in y:
                            mg += str(y["title"]) + ":" + str(y["photoCount"]) + "\n"
                        else:
                            mg += str(y["title"]) + ":0 pieces\n"
            elif "Hapus album " in msg.text:
                gid = msg.text.replace("Hapus album ","")
                albums = cl.getAlbum(gid)["result"]["items"]
                i = 0
                if albums != []:
                    for album in albums:
                        cl.deleteAlbum(gid,album["Gid"])
                        i += 1
                if wait["lang"] == "JP":
                    cl.sendText(msg.to,str(i) + "Soal album telah dihapus")
                else:
                    cl.sendText(msg.to,str(i) + "Hapus kesulitan album🛡")
            elif msg.text.lower() == 'Group id':
                gid = cl.getGroupIdsJoined()
                h = ""
                for i in gid:
                    h += "[%s]:%s\n" % (cl.getGroup(i).name,i)
                cl.sendText(msg.to,h)
            elif msg.text.lower() == 'Bye serk':
                gid = cl.getGroupIdsJoined()
                gid = ki.getGroupIdsJoined()
                gid = ki2.getGroupIdsJoined()
                gid = ki3.getGroupIdsJoined()
                gid = ki4.getGroupIdsJoined()
                gid = ki5.getGroupIdsJoined()
                gid = ki6.getGroupIdsJoined()
                gid = ki7.getGroupIdsJoined()
                for i in gid:
                    ki.leaveGroup(i)
                    ki2.leaveGroup(i)
                    ki3.leaveGroup(i)
                    ki4.leaveGroup(i)
                    ki5.leaveGroup(i)
                    ki6.leaveGroup(i)
                    ki7.leaveGroup(i)
                if wait["lang"] == "JP":
                    cl.sendText(msg.to," Bot Sudah Keluar Di semua grup")
                else:
                    cl.sendText(msg.to,"He declined all invitations")
            elif msg.text in ["Group cancelall","Rejectall"]:
                gid = cl.getGroupIdsInvited()
                for i in gid:
                    cl.rejectGroupInvitation(i)
                if wait["lang"] == "JP":
                    cl.sendText(msg.to,"Aku menolak semua undangan")
                else:
                    cl.sendText(msg.to,"He declined all invitations")
            elif "Album deleted:" in msg.text:
                gid = msg.text.replace("Album deleted:","")
                albums = cl.getAlbum(gid)["result"]["items"]
                i = 0
                if albums != []:
                    for album in albums:
                        cl.deleteAlbum(gid,album["id"])
                        i += 1
                if wait["lang"] == "JP":
                    cl.sendText(msg.to,str(i) + "Soal album telah dihapus👈")
                else:
                    cl.sendText(msg.to,str(i) + "Hapus kesulitan album👈")
            elif msg.text in ["MProtection:on"]:
                if wait["MProtection"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Member Protection On")
                    else:
                        cl.sendText(msg.to,"done")
                else:
                   wait["MProtection"] = True
                   if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Member Protection On")
                   else:
                        cl.sendText(msg.to,"done")
            elif msg.text in ["MProtection:off"]:
                if wait["MProtection"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Member Protection Off")
                    else:
                        cl.sendText(msg.to,"done")
                else:
                   wait["MProtection"] = False
                   if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Member Protection Off")
                   else:
                        cl.sendText(msg.to,"done")
            elif msg.text in ["Backup:on","Backup on"]:
                if wait["Backup"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Already on")
                    else:
                        cl.sendText(msg.to,"Backup On")
                else:
                    wait["Backup"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Backup On")
                    else:
                        cl.sendText(msg.to,"Already on")
            elif msg.text in ["Backup:off","Backup off"]:
                if wait["Backup"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Already off")
                    else:
                        cl.sendText(msg.to,"Backup Off")
                else:
                    wait["Backup"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Backup Off")
                    else:
                        cl.sendText(msg.to,"Already off")
            elif msg.text in ["Like:on"]:
                if wait["likeOn"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Done")
                else:
                    wait["likeOn"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Already on")
            elif msg.text in ["Like:off"]:
                if wait["likeOn"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Done")
                else:
                    wait["likeOn"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Already off")
            elif msg.text in ["Auto add on","Add on"]:
                if wait["autoAdd"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Already On")
                    else:
                        cl.sendText(msg.to,"Already On👈")
                else:
                    wait["autoAdd"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Already On👈")
                    else:
                        cl.sendText(msg.to,"Already On👈")
            elif msg.text in ["Auto add off","Add off"]:
                if wait["autoAdd"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Hal ini sudah off👈")
                    else:
                        cl.sendText(msg.to,"Hal ini sudah dimatikan👈")
                else:
                    wait["autoAdd"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Already Off👈")
                    else:
                        cl.sendText(msg.to,"Untuk mengaktifkan-off👈")
            elif "Message set:" in msg.text:
                wait["message"] = msg.text.replace("Message set:","")
                cl.sendText(msg.to,"We changed the message👈")
            elif "Help set:" in msg.text:
                wait["help"] = msg.text.replace("Help set:","")
                cl.sendText(msg.to,"We changed the Help👈")
            elif "Pesan add:" in msg.text:
                wait["message"] = msg.text.replace("Pesan add:","")
                if wait["lang"] == "JP":
                    cl.sendText(msg.to,"Kami mengubah pesan🛡")
                else:
                    cl.sendText(msg.to,"Change information")
            elif msg.text in ["Pesan add cek","Message Confirmation"]:
                if wait["lang"] == "JP":
                    cl.sendText(msg.to,"Additional information is automatically set to the following \n\n" + wait["message"])
                else:
                    cl.sendText(msg.to,"Pesan tambahan otomatis telah ditetapkan sebagai berikut \n\n" + wait["message"])
            elif msg.text in ["Change","change"]:
                if wait["lang"] =="JP":
                    wait["lang"] = "TW"
                    cl.sendText(msg.to,"I changed the language to engglis👈")
                else:
                    wait["lang"] = "JP"
                    cl.sendText(msg.to,"I changed the language to indonesia👈")
            elif "Message set" in msg.text:
                c = msg.text.replace("Message set","")
                if c in [""," ","\n",None]:
                    cl.sendText(msg.to,"Is a string that can not be changed👈")
                else:
                    wait["comment"] = c
                    cl.sendText(msg.to,"This has been changed👈\n\n" + c)
            elif "Com Set:" in msg.text:
                c = msg.text.replace("Come Set:","")
                if c in [""," ","\n",None]:
                    cl.sendText(msg.to,"Merupakan string yang tidak bisa diubah👈")
                else:
                    wait["comment"] = c
                    cl.sendText(msg.to,"Ini telah diubah👈\n\n" + c)
            elif msg.text in ["Com on","Com:on","Comment on"]:
                if wait["commentOn"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Aku berada di👈")
                    else:
                        cl.sendText(msg.to,"To open👈")
                else:
                    wait["commentOn"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"ã‚ªãƒ³ã«ã—ã¾ã—ãŸ👈")
                    else:
                        cl.sendText(msg.to,"è¦äº†å¼€👈")
            elif msg.text in ["Com off"]:
                if wait["commentOn"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Hal ini sudah off")
                    else:
                        cl.sendText(msg.to,"It is already turned off")
                else:
                    wait["commentOn"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Off👈")
                    else:
                        cl.sendText(msg.to,"To turn off")
            elif msg.text in ["Comen","Comment"]:
                cl.sendText(msg.to,"Auto komentar saat ini telah ditetapkan sebagai berikut:👈\n\n" + str(wait["comment"]))
            elif msg.text in ["url","Url"]:
                if msg.toType == 2:
                    g = cl.getGroup(msg.to)
                    if g.preventJoinByTicket == True:
                        g.preventJoinByTicket = False
                        cl.updateGroup(g)
                    gurl = cl.reissueGroupTicket(msg.to)
                    cl.sendText(msg.to,"line://ti/g/" + gurl)
                else:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Hal ini tidak dapat digunakan di luar kelompok")
                    else:
                        cl.sendText(msg.to,"Tidak dapat digunakan untuk kelompok selain")
            elif "gurl+" in msg.text:
                if msg.toType == 2:
                    gid = msg.text.replace("gurl+","")
                    gurl = cl.reissueGroupTicket(gid)
                    cl.sendText(msg.to,"line://ti/g/" + gurl)
                else:
                    cl.sendText(msg.to,"ã‚°ãƒ«ãƒ¼ãƒ—ä»¥å¤–ã§ã¯ä½¿ç”¨ã§ãã¾ã›ã‚“??")
            
            elif "gurl" in msg.text:
                if msg.toType == 1:
                    tid = msg.text.replace("gurl","")
                    turl = ki.getUserTicket(tid)
                    ki.sendText(msg.to,"line://ti/p" + turl)
                else:
                    ki.sendText(msg.to,"error")

            elif "gurl" in msg.text:
                if msg.toType == 2:
                    gid = msg.text.replace("gurl","")
                    gurl = cl.reissueGroupTicket(gid)
                    cl.sendText(msg.to,"line://ti/g/" + gurl)
                else:
                    cl.sendText(msg.to,"Tidak dapat digunakan untuk kelompok selain")
            elif msg.text in ["Bladd"]:
                wait["wblack"] = True
                cl.sendText(msg.to,"Please send contacts from the person you want to add to the blacklistô€œô€…”👈")
            elif msg.text in ["Bldel"]:
                wait["dblack"] = True
                cl.sendText(msg.to,"Please send contacts from the person you want to add from the blacklistô€œô€…”👈")

            elif msg.text in ["Bl cek"]:
                if wait["commentBlack"] == {}:
                    cl.sendText(msg.to,"Nothing in the blacklistô€œ🛡")
                else:
                    cl.sendText(msg.to,"The following is a blacklistô€œ👈")
                    kontak = cl.getContacts(commentBlack)
                num=1
                msgs="User Blacklist List\n"
                for ids in kontak:
                    msgs+="\n%i. %s" % (num, ids.displayName)
                    num=(num+1)
                msgs+="\n\nTotal %i blacklist user(s)" % len(kontak)
                cl.sendText(msg.to, msgs)

            elif msg.text.lower() == 'jam on':
                if wait["clock"] == True:
                    cl.sendText(msg.to,"Sudah On")
                else:
                    wait["clock"] = True
                    now2 = datetime.now()
                    nowT = datetime.strftime(now2,"(%H:%M)")
                    profile = cl.getProfile()
                    profile.displayName = wait["cName"] + nowT
                    cl.updateProfile(profile)
                    cl.sendText(msg.to,"👉Jam on👈")
            elif msg.text.lower() == 'jam off':
                if wait["clock"] == False:
                    cl.sendText(msg.to,"Hal ini sudah off🛡")
                else:
                    wait["clock"] = False
                    cl.sendText(msg.to,"Adalah Off")
            elif "Jam say:" in msg.text:
                n = msg.text.replace("Jam say:","")
                if len(n.decode("utf-8")) < 30:
                    cl.sendText(msg.to,"terlalu lama")
                else:
                    wait["cName"] = n
                    cl.sendText(msg.to,"Ini telah diubah🛡\n\n" + n)
            elif msg.text.lower() == 'up':
                if wait["clock"] == True:
                    now2 = datetime.now()
                    nowT = datetime.strftime(now2,"(%H:%M)")
                    profile = cl.getProfile()
                    profile.displayName = wait["cName"] + nowT
                    cl.updateProfile(profile)
                    cl.sendText(msg.to,"Diperbarui👈")
                else:
                    cl.sendText(msg.to,"Silahkan Aktifkan Nama")

                elif msg.text == "Cctv On":
                    cl.sendText(msg.to, "Set point.")
                    try:
                        del wait2['readPoint'][msg.to]
                        del wait2['readMember'][msg.to]
                    except:
                           pass
                    now2 = datetime.now()
                    wait2['readPoint'][msg.to] = msg.id
                    wait2['readMember'][msg.to] = ""
                    wait2['setTime'][msg.to] = datetime.now().strftime('%Y-%m-%d %H:%M')
                    wait2['ROM'][msg.to] = {}
                    print wait2

                    elif msg.text == "Ciduk":
                    if msg.to in wait2['readPoint']:
                        if wait2["ROM"][msg.to].items() == []:
                            chiya = ""
                        else:
                            chiya = ""
                            for rom in wait2["ROM"][msg.to].items():
                                print rom
                                chiya += rom[1] + "\n"
                        cl.sendText(msg.to, "╔═══════════════%s\n╠════════════════\n%s╠═══════════════\n║Readig point creation:\n║ [%s]\n╚════════════════"  % (wait2['readMember'][msg.to],chiya,setTime[msg.to]))
                    else:
                        cl.sendText(msg.to, "Ketik Cctv On dulu dudul Baru bilang Ciduk Point.")
#VIEWSEEN TARO DISINI
#-----------------------------------------------
            elif "Add staff @" in msg.text:
                if msg.from_ in Bots:
                    print "[Command]Staff add executing"
                    _name = msg.text.replace("Add staff @","")
                    _nametarget = _name.rstrip('  ')
                    gs = cl.getGroup(msg.to)
                    gs = ki.getGroup(msg.to)
                    gs = ki2getGroup(msg.to)
                    gs = ki3.getGroup(msg.to)
                    gs = ki4.getGroup(msg.to)
                    gs = ki5.getGroup(msg.to)
                    gs = ki6.getGroup(msg.to)
                    targets = []
                    for g in gs.members:
                        if _nametarget == g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        ki.sendText(msg.to,"Contact not found")
                    else:
                        for target in targets:
                            try:
                                staff.append(target)
                                cl.sendText(msg.to,"Added to the staff list")
                            except:
                                pass
                    print "[Command]Staff add executed"
                else:
                    cl.sendText(msg.to,"Command denied.")
                    cl.sendText(msg.to,"Admin permission required.")
                    
            elif "Remove staff @" in msg.text:
                if msg.from_ in Bots:
                    print "[Command]Staff remove executing"
                    _name = msg.text.replace("Remove staff @","")
                    _nametarget = _name.rstrip('  ')
                    gs = cl.getGroup(msg.to)
                    gs = ki.getGroup(msg.to)
                    gs = ki2getGroup(msg.to)
                    gs = ki3.getGroup(msg.to)
                    gs = ki4.getGroup(msg.to)
                    gs = ki5.getGroup(msg.to)
                    gs = ki6.getGroup(msg.to)
                    targets = []
                    for g in gs.members:
                        if _nametarget == g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        ki.sendText(msg.to,"Contact not found")
                    else:
                        for target in targets:
                            try:
                                staff.remove(target)
                                cl.sendText(msg.to,"Removed to the staff list")
                            except:
                                pass
                    print "[Command]Staff remove executed"
                else:
                    cl.sendText(msg.to,"Command denied.")
                    cl.sendText(msg.to,"Admin permission required.")
                    
            elif "Add admin @" in msg.text:
                if msg.from_ in Bots:
                    print "[Command]admin add executing"
                    _name = msg.text.replace("Add admin @","")
                    _nametarget = _name.rstrip('  ')
                    gs = cl.getGroup(msg.to)
                    gs = ki.getGroup(msg.to)
                    gs = ki2getGroup(msg.to)
                    gs = ki3.getGroup(msg.to)
                    gs = ki4.getGroup(msg.to)
                    gs = ki5.getGroup(msg.to)
                    gs = ki6.getGroup(msg.to)
                    targets = []
                    for g in gs.members:
                        if _nametarget == g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        ki.sendText(msg.to,"Contact not found")
                    else:
                        for target in targets:
                            try:
                                staff.append(target)
                                cl.sendText(msg.to,"Added to the admin list")
                            except:
                                pass
                    print "[Command]admin add executed"
                else:
                    cl.sendText(msg.to,"Command denied.")
                    cl.sendText(msg.to,"Admin permission required.")
                    
            elif "Remove admin @" in msg.text:
                if msg.from_ in Bots:
                    print "[Command]admin remove executing"
                    _name = msg.text.replace("Remove admin @","")
                    _nametarget = _name.rstrip('  ')
                    gs = cl.getGroup(msg.to)
                    gs = ki.getGroup(msg.to)
                    gs = ki2getGroup(msg.to)
                    gs = ki3.getGroup(msg.to)
                    gs = ki4.getGroup(msg.to)
                    gs = ki5.getGroup(msg.to)
                    gs = ki6.getGroup(msg.to)
                    targets = []
                    for g in gs.members:
                        if _nametarget == g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        ki.sendText(msg.to,"Contact not found")
                    else:
                        for target in targets:
                            try:
                                staff.remove(target)
                                cl.sendText(msg.to,"Removed to the admin list")
                            except:
                                pass
                    print "[Command]admin remove executed"
                else:
                    cl.sendText(msg.to,"Command denied.")
                    cl.sendText(msg.to,"Admin permission required.")
                    
            elif msg.text in ["Stafflist","stafflist"]:
                if staff == []:
                    ki.sendText(msg.to,"The stafflist is empty")
                else:
                    ki.sendText(msg.to,"Staff list:")
                    mc = ""
                    for mi_d in staff:
                        mc += "->" +cl.getContact(mi_d).displayName + "\n"
                    ki.sendText(msg.to,mc)
                    print "[Command]Stafflist executed"
            
            elif msg.text in ["Admin list","admin list"]:
                if admin == []:
                    ki.sendText(msg.to,"The stafflist is empty")
                else:
                    ki.sendText(msg.to,"Admin list:")
                    mc = ""
                    for mi_d in staff:
                        mc += "->" +cl.getContact(mi_d).displayName + "\n"
                    ki.sendText(msg.to,mc)
                    print "[Command]Adminlist executed"
                    
            #elif msg.text in ["Ip Like", "Ar like"]:
                #if msg.from_ in staff:
                    #print "[Command]Like executed"
                    #cl.sendText(msg.to,"Trying to Like post(s) from staff")
                    #try:
                        #likePost()
                    #except:
                        #pass
#batas__________________

            elif "staff add @" in msg.text:
                if msg.from_ in admin:
                    print "[Command]Staff add executing"
                    _name = msg.text.replace("Ar staff add @","")
                    _nametarget = _name.rstrip('  ')
                    gs = cl.getGroup(msg.to)
                    gs = ki.getGroup(msg.to)
                    gs = ki2.getGroup(msg.to)
                    gs = ki3.getGroup(msg.to)
                    gs = ki4.getGroup(msg.to)
                    gs = ki5.getGroup(msg.to)
                    gs = ki6.getGroup(msg.to)
                    targets = []
                    for g in gs.members:
                        if _nametarget == g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        ki.sendText(msg.to,"Contact not found")
                    else:
                        for target in targets:
                            try:
                                staff.append(target)
                                cl.sendText(msg.to,"Added to the staff list")
                            except:
                                pass
                    print "[Command]Staff add executed"
                else:
                    cl.sendText(msg.to,"Command denied.")
                    cl.sendText(msg.to,"Admin permission required.")
#------------------tes coba staf----------bawah
            elif "Staff add @" in msg.text:
                if msg.from_ in admin:
                    print "[Command]Staff add executing"
                    _name = msg.text.replace("Staff add @","")
                    _nametarget = _name.rstrip('  ')
                    gs = cl.getGroup(msg.to)
                    gs = ki.getGroup(msg.to)
                    gs = ki1.getGroup(msg.to)
                    gs = ki2.getGroup(msg.to)
                    gs = ki3.getGroup(msg.to)
                    gs = ki4.getGroup(msg.to)
                    gs = ki6.getGroup(msg.to)
                    targets = []
                    for g in gs.members:
                        if _nametarget == g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        ki.sendText(msg.to,"Contact not found")
                    else:
                        for target in targets:
                            try:
                                staff.append(target)
                                cl.sendText(msg.to,"Added to the staff list")
                            except:
                                pass
                    print "[Command]Staff add executed"
                else:
                    cl.sendText(msg.to,"Command denied.")
                    cl.sendText(msg.to,"Admin permission required.")

            elif "staff remove @" in msg.text:
                if msg.from_ in admin:
                    print "[Command]Staff remove executing"
                    _name = msg.text.replace("staff remove @","")
                    _nametarget = _name.rstrip('  ')
                    gs = cl.getGroup(msg.to)
                    gs = ki.getGroup(msg.to)
                    gs = ki1.getGroup(msg.to)
                    gs = ki2.getGroup(msg.to)
                    gs = ki3.getGroup(msg.to)
                    gs = ki4.getGroup(msg.to)
                    gs = ki5.getGroup(msg.to)
                    gs = ki6.getGroup(msg.to)
                    targets = []
                    for g in gs.members:
                        if _nametarget == g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        ki.sendText(msg.to,"Contact not found")
                    else:
                        for target in targets:
                            try:
                                staff.remove(target)
                                cl.sendText(msg.to,"Removed to the staff list")
                            except:
                                pass
                    print "[Command]Staff remove executed"
                else:
                    cl.sendText(msg.to,"Command denied.")
                    cl.sendText(msg.to,"Admin permission required.")

            elif msg.text in ["Stafflist","stafflist"]:
                if staff == []:
                    cl.sendText(msg.to,"The stafflist is empty")
                else:
                    cl.sendText(msg.to,"Staff list:")
                    mc = ""
                    for mi_d in staff:
                        mc += "->" +cl.getContact(mi_d).displayName + "\n"
                    cl.sendText(msg.to,mc)
                    print "[Command]Stafflist executed"

#----------------------------------------------- atas              
            elif "Sory " in msg.text:
                if msg.toType == 2:
                  if msg.from_ in admin:
                     key = eval(msg.contentMetadata["MENTION"])
                     key["MENTIONEES"][0]["M"]
                     targets = []
                     for x in key["MENTIONEES"]:
                         targets.append(x["M"])
                     for target in targets:
                        try:
                           klist=[ki,ki1,ki2,ki3,ki4,ki5,ki6,ki7]
                           kicker = random.choice(klist)
                           if msg.from_ not in target:
                             kicker.kickoutFromGroup(msg.to,[target])
                             print (msg.to,[g.mid])
                        except:
                             ki.sendText(msg.to,"ops... \nSorry.... \ Aim khilaf......")
            elif "Say " in msg.text:
                       nk0 = msg.text.replace("Say ","")
                       nk1 = nk0.lstrip()
                       nk2 = nk1.replace("@","")
                       nk3 = nk2.rstrip()
                       _name = nk3
                       gs = cl.getGroup(msg.to)
                       ginfo = cl.getGroup(msg.to)
                       gs.preventJoinByTicket = False
                       cl.updateGroup(gs)
                       invsend = 0
                       Ticket = cl.reissueGroupTicket(msg.to)
                       ki7.acceptGroupInvitationByTicket(msg.to,Ticket)
                       time.sleep(0.2)
                       targets = []
                       for s in gs.members:
                           if _name in s.displayName:
                              targets.append(s.mid)
                       if targets == []:
                           sendMessage(msg.to,"user does not exist")
                           pass
                       else:
                           for target in targets:
                                try:
                                    ki7.kickoutFromGroup(msg.to,[target])
                                    print (msg.to,[g.mid])
                                except:
                                    ki7.leaveGroup(msg.to)
                                    gs = cl.getGroup(msg.to)
                        	    gs.preventJoinByTicket = True
                        	    cl.updateGroup(gs)
                                    gs.preventJoinByTicket(gs)
                        	    cl.updateGroup(gs)
#-----------------------------------------------------------
            elif "Bunuh " in msg.text:
                   targets = []
                   key = eval(msg.contentMetadata["MENTION"])
                   key["MENTIONEES"][0]["M"]
                   for x in key["MENTIONEES"]:
                       targets.append(x["M"])
                   for target in targets:
                       try:
                           ki.kickoutFromGroup(msg.to,[target])
                           ki2.kickoutFromGroup(msg.to,[target])
                       except:
                           ki.sendText(msg.to,"Error")
            elif "Cek " in msg.text:
                   key = eval(msg.contentMetadata["MENTION"])
                   key1 = key["MENTIONEES"][0]["M"]
                   mi = cl.getContact(key1)
                   cl.sendText(msg.to,"Mid:" +  key1)

            elif "Beb " in msg.text:                  
                       nk0 = msg.text.replace("Beb ","")
                       nk1 = nk0.lstrip()
                       nk2 = nk1.replace("","")
                       nk3 = nk2.rstrip()
                       _name = nk3
                       gs = cl.getGroup(msg.to)
                       targets = []
                       for s in gs.members:
                           if _name in s.displayName:
                              targets.append(s.mid)
                       if targets == []:
                           sendMessage(msg.to,"user does not exist")
                           pass
                       else:
                           for target in targets:
                                try:
                                    random.choice(KAC).kickoutFromGroup(msg.to,[target])
                                    print (msg.to,[g.mid])
                                except:
                                    cl.sendText(msg.to,"Good Bye")
#-----------------------------------------------------------
            elif "Stalk " in msg.text:
                 print "[Command]Stalk executing"
                 stalkID = msg.text.replace("Stalk ","")
                 subprocess.call(["instaLooter",stalkID,"tmp/","-n","1"])   
                 files = glob.glob("tmp/*.jpg")
                 for file in files:
                     os.rename(file,"tmp/tmp.jpg")
                 fileTmp = glob.glob("tmp/tmp.jpg")
                 if not fileTmp:
                     cl.sendText(msg.to, "Image not found, maybe the account haven't post a single picture or the account is private")
                     print "[Command]Stalk,executed - no image found"
                 else:
                     image = upload_tempimage(client)
                     cl.sendText(msg.to, format(image['link']))
                     subprocess.call(["sudo","rm","-rf","tmp/tmp.jpg"])
                     print "[Command]Stalk executed - succes"
#-----------------------------------------------------------
            elif "InviteMeTo: " in msg.text:
                if msg.from_ in creator:
                    gid = msg.text.replace("InviteMeTo: ","")
                    if gid == "":
                        cl.sendText(msg.to,"Invalid group id")
                    else:
                        try:
                            cl.findAndAddContactsByMid(msg.from_)
                            cl.inviteIntoGroup(gid,[msg.from_])
                        except:
                            cl.sendText(msg.to,"Mungkin saya tidak di dalaam grup itu")
#-----------------------------------------------------------
            elif "/removechat" in msg.text.lower():
                if msg.from_ in admin:
                    try:
                        cl.removeAllMessages(op.param2)
                        print "[Command] Remove Chat"
                        cl.sendText(msg.to,"Done")
                    except Exception as error:
                        print error
                        cl.sendText(msg.to,"Error")
#-----------------------------------------------------------
	        elif "Ban @" in msg.text:
                if msg.toType == 2:
                    print "[Ban]ok"
                    _name = msg.text.replace("Ban @","")
                    _nametarget = _name.rstrip()
                    gs = cl.getGroup(msg.to)
                    targets = []
                    for g in gs.members:
                        if _nametarget == g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        cl.sendText(msg.to,"Not found")
                    else:
                        for target in targets:
                            try:
                                wait["blacklist"][target] = True
                                f=codecs.open('st2__b.json','w','utf-8')
                                json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                                cl.sendText(msg.to,"Target Locked")
                            except:
                                cl.sendText(msg.to,"Success band...")
	        elif "Unban @" in msg.text:
                if msg.toType == 2:
                    print "[Unban]ok"
                    _name = msg.text.replace("Unban @","")
                    _nametarget = _name.rstrip()
                    gs = cl.getGroup(msg.to)
                    targets = []
                    for g in gs.members:
                        if _nametarget == g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        cl.sendText(msg.to,"Not found")
                    else:
                        for target in targets:
                            try:
                                del wait["blacklist"][target]
                                f=codecs.open('st2__b.json','w','utf-8')
                                json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                                cl.sendText(msg.to,"Target Unlocked")
                            except:
                                cl.sendText(msg.to,"Success unband..")
            elif "Ban:" in msg.text:                  
                       nk0 = msg.text.replace("Ban:","")
                       nk1 = nk0.lstrip()
                       nk2 = nk1.replace("","")
                       nk3 = nk2.rstrip()
                       _name = nk3
                       gs = cl.getGroup(msg.to)
                       targets = []
                       for s in gs.members:
                           if _name in s.displayName:
                              targets.append(s.mid)
                       if targets == []:
                           sendMessage(msg.to,"user does not exist")
                           pass
                       else:
                           for target in targets:
                                try:
									wait["blacklist"][target] = True
									f=codecs.open('st2__b.json','w','utf-8')
									json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
									cl.sendText(msg.to,"Target Locked")
                                except:
                                    cl.sendText(msg.to,"Success band")
            elif "Unban:" in msg.text:                  
                       nk0 = msg.text.replace("Unban:","")
                       nk1 = nk0.lstrip()
                       nk2 = nk1.replace("","")
                       nk3 = nk2.rstrip()
                       _name = nk3
                       gs = cl.getGroup(msg.to)
                       targets = []
                       for s in gs.members:
                           if _name in s.displayName:
                              targets.append(s.mid)
                       if targets == []:
                           sendMessage(msg.to,"user does not exist")
                           pass
                       else:
                           for target in targets:
                                try:
									del wait["blacklist"][target]
									f=codecs.open('st2__b.json','w','utf-8')
									json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
									cl.sendText(msg.to,"Target Unlocked")
                                except:
                                    cl.sendText(msg.to,"Success unband..")
#-----------------------------------------------------------
            elif msg.text in ["Respon","respon","responsename"]:
                cl.sendText(msg.to,"ƊƛƑƬƛƦ ƛƘƲƝ ƁƠƬ S͟͟͟͞͞͞E͟͟͟͞͞͞R͟͟͟͞͞͞K͟͟͟͞͞͞ V.2.9 👇👇")
                cl.sendText(msg.to,"ƁƠƬ S͟͟͟͞͞͞E͟͟͟͞͞͞R͟͟͟͞͞͞K͟͟͟͞͞͞ 1")
                ki.sendText(msg.to,"ƁƠƬ S͟͟͟͞͞͞E͟͟͟͞͞͞R͟͟͟͞͞͞K͟͟͟͞͞͞ 2")
                ki2.sendText(msg.to,"ƁƠƬ S͟͟͟͞͞͞E͟͟͟͞͞͞R͟͟͟͞͞͞K͟͟͟͞͞͞ 3")
                ki3.sendText(msg.to,"ƁƠƬ S͟͟͟͞͞͞E͟͟͟͞͞͞R͟͟͟͞͞͞K͟͟͟͞͞͞ 4")    
                ki4.sendText(msg.to,"ƁƠƬ S͟͟͟͞͞͞E͟͟͟͞͞͞R͟͟͟͞͞͞K͟͟͟͞͞͞ 5")
                ki5.sendText(msg.to,"ƁƠƬ S͟͟͟͞͞͞E͟͟͟͞͞͞R͟͟͟͞͞͞K͟͟͟͞͞͞ 6")
                ki6.sendText(msg.to,"ƁƠƬ S͟͟͟͞͞͞E͟͟͟͞͞͞R͟͟͟͞͞͞K͟͟͟͞͞͞ 7")
                ki7.sendText(msg.to,"ƁƠƬ S͟͟͟͞͞͞E͟͟͟͞͞͞R͟͟͟͞͞͞K͟͟͟͞͞͞ 8")
                #cl.sendText(msg.to,"Luffy On")
                cl.sendText(msg.to, "•••")
                ki.sendText(msg.to, "••••")
                ki2.sendText(msg.to,"•••••")
                ki3.sendText(msg.to,"••••••")
                ki3.sendText(msg.to,"•••••••")
                ki4.sendText(msg.to,"••••••••")
                ki5.sendText(msg.to,"•••••••••")
                ki6.sendText(msg.to,"••••••••••")
                ki7.sendText(msg.to,"•••••••••••")
                cl.sendText(msg.to,"Respon Complete")
#-----------------------------------------------------------
            elif "Pict group " in msg.text:
                saya = msg.text.replace('Pict group ','')
                gid = cl.getGroupIdsJoined()
                for i in gid:
                    h = cl.getGroup(i).name
                    gna = cl.getGroup(i)
                    if h == saya:
                        cl.sendImageWithURL(msg.to,"http://dl.profile.line.naver.jp/"+ gna.pictureStatus)
#-----------------------------------------------------------
            elif msg.text in ["Haha","Hahaha","haha"]:
                ki.sendText(msg.to,"Bau ih, jangan ketawa.")

            elif msg.text in ["Wkwkwk","wkwkwk","Wkwk","wkwk","Wkwwk"]:
                ki.sendText(msg.to,"Ga ada yang lucu ko ketawa? Situ waras?􏿿")
#-----------------------------------------------
            elif "Pap set:" in msg.text:
                wait["Pap"] = msg.text.replace("Pap set:","")
                kyu.sendText(msg.to,"Pap Has Ben Set To")

            elif msg.text in [".Pap","Pap"]:
                kyu.sendImageWithURL(msg.to,wait["Pap"])
#-----------------------------------------------
            elif msg.text in ["Kalender"]:
                wait2['setTime'][msg.to] = datetime.today().strftime('TANGGAL : %Y-%m-%d \nHARI : %A \nJAM : %H:%M:%S')
                cl.sendText(msg.to, "╔═══════════════%s\n╠════════════════KALENDER\n\n" + (wait2['setTime'][msg.to]))
#-----------------------------------------------
            elif "Mban:" in msg.text:
                midd = msg.text.replace("Mban:","")
                wait["blacklist"][midd] = True
		        cl.sendText(msg.to,"Target Lock")
#-----------------------------------------------
#-----------------------------------------------
            elif ".Youtube " in msg.text:
                 query = msg.text.replace(".Youtube ","")
                 with requests.session() as s:
                     s.headers['user-agent'] = 'Mozilla/5.0'
                     url    = 'http://www.youtube.com/results'
                     params = {'search_query': query}
                     r    = s.get(url, params=params)
                     soup = BeautifulSoup(r.content, 'html5lib')
                     for a in soup.select('.yt-lockup-title > a[title]'):
                         if '&List' not in a['href']:
                            cl.sendText(msg.to,'http://www.youtube.com' + a['href'] + a['title'])
#--------------------------------------------------------
            elif "/steal home @" in msg.text:
                print "[Command]dp executing"
                _name = msg.text.replace("/steal home @","")
                _nametarget = _name.rstrip('  ')
                gs = cl.getGroup(msg.to)
                targets = []
                for g in gs.members:
                    if _nametarget == g.displayName:
                        targets.append(g.mid)
                if targets == []:
                    ki.sendText(msg.to,"Contact not found")
                else:
                    for target in targets:
                        try:
                            contact = cl.getContact(target)
                            cu = cl.channel.getCover(target)
                            path = str(cu)
                            cl.sendImageWithURL(msg.to, path)
                        except:
                            pass
                print "[Command]dp executed"
#------------------------------------------------------------------
            elif "/steal dp @" in msg.text:
                print "[Command]dp executing"
                _name = msg.text.replace("/steal dp @","")
                _nametarget = _name.rstrip('  ')
                gs = cl.getGroup(msg.to)
                targets = []
                for g in gs.members:
                    if _nametarget == g.displayName:
                        targets.append(g.mid)
                if targets == []:
                    ki.sendText(msg.to,"Contact not found")
                else:
                    for target in targets:
                        try:
                            contact = cl.getContact(target)
                            path = "http://dl.profile.line-cdn.net/" + contact.pictureStatus
                            cl.sendImageWithURL(msg.to, path)
                        except:
                            pass
                print "[Command]dp executed"                  
#------------------------------------------------------------------
            elif "Spam @" in msg.text:
                _name = msg.text.replace("Spam @","")
                _nametarget = _name.rstrip(' ')
                gs = cl.getGroup(msg.to)
                for g in gs.members:
                    if _nametarget == g.displayName:
                       cl.sendText(msg.to,"ƠƬƜ ƧƤƛM ƬƛƦƓЄƬ 😂")
                       ki.sendText(g.mid,"Spam  😂")  
                       ki2.sendText(g.mid,"Spam  😂")  
                       ki3.sendText(g.mid,"Spam  😂")
                       ki4.sendText(g.mid,"Spam  😂")
                       ki5.sendText(g.mid,"Spam  😂")
                       ki6.sendText(g.mid,"Spam  😂")
                       ki.sendText(g.mid,"Spam  😂")  
                       ki2.sendText(g.mid,"Spam  😂")  
                       ki3.sendText(g.mid,"Spam  😂")
                       ki4.sendText(g.mid,"Spam  😂")
                       ki5.sendText(g.mid,"Spam  😂")
                       ki6.sendText(g.mid,"Spam  😂")
                       ki.sendText(g.mid,"Spam  😂")  
                       ki2.sendText(g.mid,"Spam  😂")  
                       ki3.sendText(g.mid,"Spam  😂")
                       ki4.sendText(g.mid,"Spam  😂")
                       ki5.sendText(g.mid,"Spam  😂")
                       ki6.sendText(g.mid,"Spam  😂")
                       ki.sendText(g.mid,"Spam  😂")  
                       ki2.sendText(g.mid,"Spam  😂")  
                       ki3.sendText(g.mid,"Spam  😂")
                       ki4.sendText(g.mid,"Spam  😂")
                       ki5.sendText(g.mid,"Spam  😂")
                       ki6.sendText(g.mid,"Spam  😂")
                       ki.sendText(g.mid,"Spam  😂")  
                       ki2.sendText(g.mid,"Spam  😂")  
                       ki3.sendText(g.mid,"Spam  😂")
                       ki4.sendText(g.mid,"Spam  😂")
                       ki5.sendText(g.mid,"Spam  😂")
                       ki6.sendText(g.mid,"Spam  😂")
                       ki.sendText(g.mid,"Spam  😂")  
                       ki2.sendText(g.mid,"Spam  😂")  
                       ki3.sendText(g.mid,"Spam  😂")
                       ki4.sendText(g.mid,"Spam  😂")
                       ki5.sendText(g.mid,"Spam  😂")
                       ki6.sendText(g.mid,"Spam  😂")
                       ki.sendText(g.mid,"Spam  😂")  
                       ki2.sendText(g.mid,"Spam  😂")  
                       ki3.sendText(g.mid,"Spam  😂")
                       ki4.sendText(g.mid,"Spam  😂")
                       ki5.sendText(g.mid,"Spam  😂")
                       ki6.sendText(g.mid,"Spam  😂")
                       ki.sendText(g.mid,"Spam  😂")  
                       ki2.sendText(g.mid,"Spam  😂")  
                       ki3.sendText(g.mid,"Spam  😂")
                       ki4.sendText(g.mid,"Spam  😂")
                       ki5.sendText(g.mid,"Spam  😂")
                       ki6.sendText(g.mid,"Spam  😂")
                       ki.sendText(g.mid,"Spam  😂")  
                       ki2.sendText(g.mid,"Spam  😂")  
                       ki3.sendText(g.mid,"Spam  😂")
                       ki4.sendText(g.mid,"Spam  😂")
                       ki5.sendText(g.mid,"Spam  😂")
                       ki6.sendText(g.mid,"Spam  😂")
                       ki.sendText(g.mid,"HƛHƛHƛ ƊƖ ƧƤƛM  😂")
                       ki2.sendText(g.mid,"HƛHƛHƛ ƊƖ ƧƤƛM  😂")
                       ki3.sendText(g.mid,"HƛHƛHƛ ƊƖ ƧƤƛM  😂")
                       ki.sendText(g.mid,"Spam  😂")  
                       ki2.sendText(g.mid,"Spam  😂")  
                       ki3.sendText(g.mid,"Spam  😂")
                       ki4.sendText(g.mid,"Spam  😂")
                       ki5.sendText(g.mid,"Spam  😂")
                       ki6.sendText(g.mid,"Spam  😂")
                       ki.sendText(g.mid,"Spam  😂")  
                       ki2.sendText(g.mid,"Spam  😂")  
                       ki3.sendText(g.mid,"Spam  😂")
                       ki4.sendText(g.mid,"Spam  😂")
                       ki5.sendText(g.mid,"Spam  😂")
                       ki6.sendText(g.mid,"Spam  😂")
                       ki.sendText(g.mid,"Spam  😂")  
                       ki2.sendText(g.mid,"Spam  😂")  
                       ki3.sendText(g.mid,"Spam  😂")
                       ki4.sendText(g.mid,"Spam  😂")
                       ki5.sendText(g.mid,"Spam  😂")
                       ki6.sendText(g.mid,"Spam  😂")
                       ki.sendText(g.mid,"Spam  😂")  
                       ki2.sendText(g.mid,"Spam  😂")  
                       ki3.sendText(g.mid,"Spam  😂")
                       ki4.sendText(g.mid,"Spam  😂")
                       ki5.sendText(g.mid,"Spam  😂")
                       ki6.sendText(g.mid,"Spam  😂")
                       ki.sendText(g.mid,"Spam  😂")  
                       ki2.sendText(g.mid,"Spam  😂")  
                       ki3.sendText(g.mid,"Spam  😂")
                       ki4.sendText(g.mid,"Spam  😂")
                       ki5.sendText(g.mid,"Spam  😂")
                       ki6.sendText(g.mid,"Spam  😂")
                       ki.sendText(g.mid,"Spam  😂")  
                       ki2.sendText(g.mid,"Spam  😂")  
                       ki3.sendText(g.mid,"Spam  😂")
                       ki4.sendText(g.mid,"Spam  😂")
                       ki5.sendText(g.mid,"Spam  😂")
                       ki6.sendText(g.mid,"Spam  😂")
                       ki.sendText(g.mid,"Spam  😂")  
                       ki2.sendText(g.mid,"Spam  😂")  
                       ki3.sendText(g.mid,"Spam  😂")
                       ki4.sendText(g.mid,"Spam  😂")
                       ki5.sendText(g.mid,"Spam  😂")
                       ki6.sendText(g.mid,"Spam  😂")
                       ki.sendText(g.mid,"Spam  😂")  
                       ki2.sendText(g.mid,"Spam  😂")  
                       ki3.sendText(g.mid,"Spam  😂")
                       ki4.sendText(g.mid,"Spam  😂")
                       ki5.sendText(g.mid,"Spam  😂")
                       ki6.sendText(g.mid,"Spam  😂")
                       ki.sendText(g.mid,"Spam  😂")  
                       ki2.sendText(g.mid,"Spam  😂")  
                       ki3.sendText(g.mid,"Spam  😂")
                       ki4.sendText(g.mid,"Spam  😂")
                       ki5.sendText(g.mid,"Spam  😂")
                       ki6.sendText(g.mid,"Spam  😂")
                       ki.sendText(g.mid,"HƛHƛHƛ ƊƖ ƧƤƛM  😂")
                       ki2.sendText(g.mid,"HƛHƛHƛ ƊƖ ƧƤƛM  😂")
                       ki3.sendText(g.mid,"HƛHƛHƛ ƊƖ ƧƤƛM  😂")
                       ki.sendText(g.mid,"Spam  😂")  
                       ki2.sendText(g.mid,"Spam  😂")  
                       ki3.sendText(g.mid,"Spam  😂")
                       ki4.sendText(g.mid,"Spam  😂")
                       ki5.sendText(g.mid,"Spam  😂")
                       ki6.sendText(g.mid,"Spam  😂")
                       ki.sendText(g.mid,"Spam  😂")  
                       ki2.sendText(g.mid,"Spam  😂")  
                       ki3.sendText(g.mid,"Spam  😂")
                       ki4.sendText(g.mid,"Spam  😂")
                       ki5.sendText(g.mid,"Spam  😂")
                       ki6.sendText(g.mid,"Spam  😂")
                       ki.sendText(g.mid,"Spam  😂")  
                       ki2.sendText(g.mid,"Spam  😂")  
                       ki3.sendText(g.mid,"Spam  😂")
                       ki4.sendText(g.mid,"Spam  😂")
                       ki5.sendText(g.mid,"Spam  😂")
                       ki6.sendText(g.mid,"Spam  😂")
                       ki.sendText(g.mid,"Spam  😂")  
                       ki2.sendText(g.mid,"Spam  😂")  
                       ki3.sendText(g.mid,"Spam  😂")
                       ki4.sendText(g.mid,"Spam  😂")
                       ki5.sendText(g.mid,"Spam  😂")
                       ki6.sendText(g.mid,"Spam  😂")
                       ki.sendText(g.mid,"Spam  😂")  
                       ki2.sendText(g.mid,"Spam  😂")  
                       ki3.sendText(g.mid,"Spam  😂")
                       ki4.sendText(g.mid,"Spam  😂")
                       ki5.sendText(g.mid,"Spam  😂")
                       ki6.sendText(g.mid,"Spam  😂")
                       ki.sendText(g.mid,"Spam  😂")  
                       ki2.sendText(g.mid,"Spam  😂")  
                       ki3.sendText(g.mid,"Spam  😂")
                       ki4.sendText(g.mid,"Spam  😂")
                       ki5.sendText(g.mid,"Spam  😂")
                       ki6.sendText(g.mid,"Spam  😂")
                       ki.sendText(g.mid,"Spam  😂")  
                       ki2.sendText(g.mid,"Spam  😂")  
                       ki3.sendText(g.mid,"Spam  😂")
                       ki4.sendText(g.mid,"Spam  😂")
                       ki5.sendText(g.mid,"Spam  😂")
                       ki6.sendText(g.mid,"Spam  😂")
                       ki.sendText(g.mid,"Spam  😂")  
                       ki2.sendText(g.mid,"Spam  😂")  
                       ki3.sendText(g.mid,"Spam  😂")
                       ki4.sendText(g.mid,"Spam  😂")
                       ki5.sendText(g.mid,"Spam  😂")
                       ki6.sendText(g.mid,"Spam  😂")
                       ki.sendText(g.mid,"Spam  😂")  
                       ki2.sendText(g.mid,"Spam  😂")  
                       ki3.sendText(g.mid,"Spam  😂")
                       ki4.sendText(g.mid,"Spam  😂")
                       ki5.sendText(g.mid,"Spam  😂")
                       ki6.sendText(g.mid,"Spam  😂")
                       ki.sendText(g.mid,"HƛHƛHƛ ƊƖ ƧƤƛM  😂")
                       ki2.sendText(g.mid,"HƛHƛHƛ ƊƖ ƧƤƛM  😂")
                       ki3.sendText(g.mid,"HƛHƛHƛ ƊƖ ƧƤƛM  😂")
                       ki.sendText(g.mid,"Spam  😂")  
                       ki2.sendText(g.mid,"Spam  😂")  
                       ki3.sendText(g.mid,"Spam  😂")
                       ki4.sendText(g.mid,"Spam  😂")
                       ki5.sendText(g.mid,"Spam  😂")
                       ki6.sendText(g.mid,"Spam  😂")
                       ki.sendText(g.mid,"Spam  😂")  
                       ki2.sendText(g.mid,"Spam  😂")  
                       ki3.sendText(g.mid,"Spam  😂")
                       ki4.sendText(g.mid,"Spam  😂")
                       ki5.sendText(g.mid,"Spam  😂")
                       ki6.sendText(g.mid,"Spam  😂")
                       ki.sendText(g.mid,"Spam  😂")  
                       ki2.sendText(g.mid,"Spam  😂")  
                       ki3.sendText(g.mid,"Spam  😂")
                       ki4.sendText(g.mid,"Spam  😂")
                       ki5.sendText(g.mid,"Spam  😂")
                       ki6.sendText(g.mid,"Spam  😂")
                       ki.sendText(g.mid,"Spam  😂")  
                       ki2.sendText(g.mid,"Spam  😂")  
                       ki3.sendText(g.mid,"Spam  😂")
                       ki4.sendText(g.mid,"Spam  😂")
                       ki5.sendText(g.mid,"Spam  😂")
                       ki6.sendText(g.mid,"Spam  😂")
                       ki.sendText(g.mid,"Spam  😂")  
                       ki2.sendText(g.mid,"Spam  😂")  
                       ki3.sendText(g.mid,"Spam  😂")
                       ki4.sendText(g.mid,"Spam  😂")
                       ki5.sendText(g.mid,"Spam  😂")
                       ki6.sendText(g.mid,"Spam  😂")
                       ki.sendText(g.mid,"Spam  😂")  
                       ki2.sendText(g.mid,"Spam  😂")  
                       ki3.sendText(g.mid,"Spam  😂")
                       ki4.sendText(g.mid,"Spam  😂")
                       ki5.sendText(g.mid,"Spam  😂")
                       ki6.sendText(g.mid,"Spam  😂")
                       ki.sendText(g.mid,"Spam  😂")  
                       ki2.sendText(g.mid,"Spam  😂")  
                       ki3.sendText(g.mid,"Spam  😂")
                       ki4.sendText(g.mid,"Spam  😂")
                       ki5.sendText(g.mid,"Spam  😂")
                       ki6.sendText(g.mid,"Spam  😂")
                       ki.sendText(g.mid,"Spam  😂")  
                       ki2.sendText(g.mid,"Spam  😂")  
                       ki3.sendText(g.mid,"Spam  😂")
                       ki4.sendText(g.mid,"Spam  😂")
                       ki5.sendText(g.mid,"Spam  😂")
                       ki6.sendText(g.mid,"Spam  😂")
                       ki.sendText(g.mid,"Spam  😂")  
                       ki2.sendText(g.mid,"Spam  😂")  
                       ki3.sendText(g.mid,"Spam  😂")
                       ki4.sendText(g.mid,"Spam  😂")
                       ki5.sendText(g.mid,"Spam  😂")
                       ki6.sendText(g.mid,"Spam  😂")
                       ki.sendText(g.mid,"HƛHƛHƛ ƊƖ ƧƤƛM  😂")
                       ki2.sendText(g.mid,"HƛHƛHƛ ƊƖ ƧƤƛM  😂")
                       ki3.sendText(g.mid,"HƛHƛHƛ ƊƖ ƧƤƛM  😂")
                       cl.sendText(msg.to, "ƊƠƝЄ ƧƤƛM  😂")
                       print "Done spam" 
#--------------------------------------------------------
            elif "#END" in msg.text:
                try:
                    import sys
                    sys.exit()
                except:
                    pass
#--------------------------------------------------------
            elif "Set member: " in msg.text:
              if msg.from_ in admin:
                  jml = msg.text.replace("Set member: ","")
                  wait["Members"] = int(jml)
                  cl.sendText(msg.to, "Jumlah minimal member telah di set : "+jml)
              else:
                  cl.sendText(msg.to, "Khusus Admin")
#--------------------------------------------------------
            elif "/ig: " in msg.text.lower():
                arg = msg.text.split(' ');
                nk0 = msg.text.replace("/ig: ","")
                nk1 = nk0.rstrip('  ')
                if len(arg) > 1:
                    proc = subprocess.Popen('curl -s https://www.instagram.com/'+nk1+'/?__a=1',shell=True, stdout=subprocess.PIPE)
                    x = proc.communicate()[0]
                    parsed_json = json.loads(x)
                    if(len(x) > 10):
                        username = (parsed_json['user']['username'])
                        fullname = (parsed_json['user']['full_name'])
                        followers = (parsed_json['user']['followed_by']['count'])
                        following = (parsed_json['user']['follows']['count'])
                        media = (parsed_json['user']['media']['count'])
                        bio = (parsed_json['user']['biography'])
                        url = (parsed_json['user']['external_url'])
                        cl.sendText(msg.to,"Profile "+username+"\n\nUsername : "+username+"\nFull Name : "+fullname+"\nFollowers : "+str(followers)+"\nFollowing : "+str(following)+"\nBio : "+str(bio)+"\n\nURL : "+str(url))
                        print '[Command] Instagram'
#--------------------------------------------------------
            elif "Bc: " in msg.text:
              bc = msg.text.replace("Bc: ","")
              gid = cl.getGroupIdsJoined()
              if msg.from_ in admin:
                  for i in gid:
                      cl.sendText(i,"||=====[BROADCAST]=====||\n\n"+bc+"\n\nContact Me : line.me/ti/p/~rd.rmdhn")
                      cl.sendText(msg.to,"Success BC")
                  else:
                      cl.sendText(msg.to,"Khusus Admin")
#-------------------------------------------------------- 
            elif msg.text in ["Kernel","kernel"]:
                 if msg.from_ in admin:
                     botKernel = subprocess.Popen(["uname","-svmo"], stdout=subprocess.PIPE).communicate()[0]
                     cl.sendText(msg.to, botKernel)
                     print "[Command]Kernel executed"
#-----------------------------------------------------------
            elif '/music ' in msg.text.lower():
                try:
                    songname = msg.text.lower().replace('.music ','')
                    params = {'songname': songname}
                    r = requests.get('http://ide.fdlrcn.com/workspace/yumi-apis/joox?' + urllib.urlencode(params))
                    data = r.text
                    data = json.loads(data)
                    for song in data:
                        hasil = 'This is Your Music\n'
                        hasil += 'Judul : ' + song[0]
                        hasil += '\nDurasi : ' + song[1]
                        hasil += '\nLink Download : ' + song[4]
                        cl.sendText(msg.to, hasil)
                        cl.sendText(msg.to, "Please Wait for audio...")
                        cl.sendAudioWithURL(msg.to, song[4])
                except Exception as njer:
                        cl.sendText(msg.to, str(njer))
#--------------------------------------------------------
            elif '/lirik ' in msg.text.lower():
                try:
                    songname = msg.text.lower().replace('/lirik ','')
                    params = {'songname': songname}
                    r = requests.get('http://ide.fdlrcn.com/workspace/yumi-apis/joox?' + urllib.urlencode(param))
                    data = r.text
                    data = json.loads(data)
                    for song in data:
                        hasil = song[5]
                        cl.sendText(msg.to, hasil)
                except Exception as njer:
                        cl.sendText(msg.to, str(njer))
#--------------------------------------------------------
            elif msg.text.lower() == 'Runtime':
                eltime = time.time() - mulai
                van = "Bot Sudah Berjalan Selama "+waktu(eltime)
                cl.sendText(msg.to,van)
                
            elif msg.text is None:
                return
#--------------------------------------------------------
            elif "Add all" in msg.text:
                thisgroup = cl.getGroups([msg.to])
                Mids = [contact.mid for contact in thisgroup[0].members]
                mi_d = Mids[:33]
                cl.findAndAddContactsByMids(mi_d)
                cl.sendText(msg.to,"Success Add all")
#--------------------------------------------------------
            elif "Recover" in msg.text:
                thisgroup = cl.getGroups([msg.to])
                Mids = [contact.mid for contact in thisgroup[0].members]
                mi_d = Mids[:33]
                cl.createGroup("Recover", mi_d)
                cl.sendText(msg.to,"Success recover")
#--------------------------------------------------------
            elif msg.text in ["Remove all chat"]:
                cl.removeAllMessages(op.param2)
                cl.sendText(msg.to,"Removed all chat")
#--------------------------------------------------------
            elif "Backup me" in msg.text:
                try:
                    cl.updateDisplayPicture(profile.pictureStatus)
                    cl.updateProfile(profile)
                    cl.sendText(msg.to, "Success backup profile")
                except Exception as e:
                    cl.sendText(msg.to, str(e))
#--------------------------------------------------------
#KICK_BY_TAG
            elif "Boom " in msg.text:
              if 'MENTION' in msg.contentMetadata.keys()!= None:
                names = re.findall(r'@(\w+)', msg.text)
                mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                mentionees = mention['MENTIONEES']
                print mentionees
                for mention in mentionees:
                    cl.kickoutFromGroup(msg.to,[mention['M']])
            
#--------------------------------------------------------

            elif "Gift @" in msg.text:
                _name = msg.text.replace("Gift @","")
                _nametarget = _name.rstrip(' ')
                gs = cl.getGroup(msg.to)
                for g in gs.members:
                    if _nametarget == g.displayName:
                    msg.contentType = 9
                        msg.contentMetadata={'PRDID': '89131c1a-e549-4bd5-9e60-e24de0d2e252',
                                    'PRDTYPE': 'THEME',
                                    'MSGTPL': '10'}
                        msg.text = None
                        cl.sendMessage(msg,g)



            elif "Spamcontact @" in msg.text:
                _name = msg.text.replace("Spamcontact @","")
                _nametarget = _name.rstrip(' ')
                gs = cl.getGroup(msg.to)
                for g in gs.members:
                    if _nametarget == g.displayName:
                       cl.sendText(g.mid,"Spammed !")
                       kk.sendText(g.mid,"Spammed !") 
                       ki.sendText(g.mid,"Spammed !") 
                       kc.sendText(g.mid,"Spammed !")
                       cl.sendText(msg.to, "Done")
                       print " Spammed !"
#-----------------------------------------------------------
            elif 'Wikipedia ' in msg.text.lower():
                try:
                    wiki = msg.text.lower().replace("wikipedia ","")
                    wikipedia.set_lang("id")
                    pesan="Title ("
                    pesan+=wikipedia.page(wiki).title
                    pesan+=")\n\n"
                    pesan+=wikipedia.summary(wiki, sentences=1)
                    pesan+="\n"
                    pesan+=wikipedia.page(wiki).url
                    cl.sendText(msg.to, pesan)
                except:
                        try:
                            pesan="Over Text Limit! Please Click link\n"
                            pesan+=wikipedia.page(wiki).url
                            cl.sendText(msg.to, pesan)
                        except Exception as e:
                            cl.sendText(msg.to, str(e))
#-----------------------------------------------------------
            elif msg.text in ["Gcreator:inv"]:
                if msg.from_ in admin:
                    ginfo = cl.getGroup(msg.to)
                    gCreator = ginfo.creator.mid
                    try:
                       cl.findAndAddContactsByMid(gCreator)
                       cl.inviteIntoGroup(msg.to,[gCreator])
                       print "success inv gCreator"
                    except:
                       pass
#-----------------------------------------------------------
            elif "#leave" in msg.text:
                try:
                    import sys
                    sys.exit()
                except:
                    pass
#-----------------------------------------------------------
            elif "Absen" in msg.text:
                S0 = cl.getProfile()
                S1 = ki.getProfile()
                S2 = ki2.getProfile()
                S3 = ki3.getProfile()
                S4 = ki4.getProfile()
                S5 = ki5.getProfile()
                S6 = ki6.getProfile()
                S7 = ki7.getProfile()
                cl.sendText(msg.to, S0.displayName + " ")
                ki.sendText(msg.to, S1.displayName + " ")
                ki2.sendText(msg.to, S2.displayName + " ")
                ki3.sendText(msg.to, S3.displayName + " ")
                ki4.sendText(msg.to, S4.displayName + " ")
                ki5.sendText(msg.to, S5.displayName + " ")
                ki6.sendText(msg.to, S6.displayName + " ")
                ki7.sendText(msg.to, S7.displayName + " ")
   
                           
      #-------------Fungsi Balesan Respon Start---------------------#
            elif msg.text in ["Ini Apa","ini apa","Apaan Ini","apaan ini"]:
                ki.sendText(msg.to,"Ya gitu deh intinya mah 􀨁􀅴questioning􏿿")

      #-------------Fungsi Balesan Respon Finish---------------------#  
#-----------------------------------------------
            elif "Apakah " in msg.text:
                tanya = msg.text.replace("Apakah ","")
                jawab = ("Ya","Tidak")
                jawaban = random.choice(jawab)
                cl.sendText(msg.to,jawaban)
            elif "Rate" in msg.text:
                tanya = msg.text.replace("Rate","")
                jawab = ("10%","20%","30%","40%","50%","60%","70%","80%","90%","100%")
                jawaban = random.choice(jawab)
                cl.sendText(msg.to,jawaban)
#-------------------------------------------------------------
            elif "Dosa @" in msg.text:
                tanya = msg.text.replace("Dosa @","")
                jawab = ("Tidak ada","10%","20%","30%","40%","50%","60%","70%","80%","90%","100%","Tak terhingga")
                jawaban = random.choice(jawab)
                cl.sendText(msg.to,"Dosanya " + tanya + " adalah " + jawaban + " Tobat dong ")
            elif "Pahala @" in msg.text:
                tanya = msg.text.replace("Pahala @","")
                jawab = ("Tidak ada","10%","20%","30%","40%","50%","60%","70%","80%","90%","100%","Tak terhingga")
                jawaban = random.choice(jawab)
                cl.sendText(msg.to,"Pahalanya " + tanya + " adalah " + jawaban + "Tingkatkan lagi  ")
#-------------------------------------------------------------  
 #-----------------------------------------------                          
            elif msg.text in ["Cuma bisa ngayal"]:
                if msg.from_ in admin:
                    ki.sendText(msg.to,"Ihh jangan gitu😂")
                  
            elif msg.text in ["Besok bisa jalan?"]:
                if msg.from_ in admin:
                    ki.sendText(msg.to,"Bisa, emang mau ngapain?")
#-----------------------------------------------
            elif msg.text in ["Mau ketemu kamu aja"]:
                if msg.from_ in admin:
                    ki.sendText(msg.to,"Iya nih aku juga kangen kamu, udah lama ga ketemu..")
#-----------------------------------------------
            elif msg.text in ["Kita ketemuan dimana?"]:
                if msg.from_ in admin:
                    ki.sendText(msg.to,"Terserah kamu")
#-----------------------------------------------
            elif msg.text in ["Ihh jangan terserah geh"]:
                if msg.from_ in admin:
                    ki.sendText(msg.to,"Emm.. aku nya bingung geh")
#-----------------------------------------------
            elif msg.text in ["Yaudah kita ketemuan di lippo aja"]:
                if msg.from_ in admin:
                    ki.sendText(msg.to,"Hmm.. oke deh..")
#-----------------------------------------------
            elif msg.text in ["Seandainya..."]:
                if msg.from_ in admin:
                    ki.sendText(msg.to,"Aku bisa di samping kamu...")
#-----------------------------------------------
            elif msg.text in ["Aku bisa peluk kamu..."]:
                if msg.from_ in admin:
                    ki.sendText(msg.to,"Hehe pengen banget ya?")
#-----------------------------------------------
            elif msg.text in ["Yaiyalah pengen, siapa si yang ga mau meluk cewe secantik kamu?"]:
                if msg.from_ in admin:
                    ki.sendText(msg.to,"Ihh akumah biasa aja kali, ngga ada yang spesial")
#-----------------------------------------------
            elif msg.text in ["P"]:
                ki.sendText(msg.to,"Berisik ih􏿿")
#-----------------------------------------------
            elif msg.text in ["Kenapa sayang?"]:
                ki.sendText(msg.to,"Mereka tuh berisik banget􏿿")
#-----------------------------------------------
            elif msg.text in ["Yaudah kita lanjut pc aja sayang"]:
                ki.sendText(msg.to,"Okeeyy..")
#-----------------------------------------------
            elif msg.text in ["Adam"]:
                ki.sendText(msg.to,"Orangnya gendut, suka mukulin yang ga salah􏿿")
#-----------------------------------------------
            elif msg.text in ["Iqbal"]:
                ki.sendText(msg.to,"Bucin hahaha􏿿")
#-----------------------------------------------
            elif msg.text in ["Puri jr"]:
                ki.sendText(msg.to,"Ngga gerak lagi semenjak Dimas pindah ke Jogja:(􏿿")
#-----------------------------------------------
            elif msg.text in ["Dhani"]:
                ki.sendText(msg.to,"Ganteng orangnya. tapi sayang, dia kurus. Gitu gitu juga dia pacar saya􏿿")
#-----------------------------------------------
            elif msg.text in ["Jutek amat"]:
                ki.sendText(msg.to,"Biarin.􏿿")
#-----------------------------------------------
            elif msg.text in ["Lagi pms ya?"]:
                ki.sendText(msg.to,"Iya emang kenapa? masalah?")
#-----------------------------------------------
            elif msg.text in ["Biasa aja dong"]:
                ki.sendText(msg.to,"Hehe yaudah maaf.")
#-----------------------------------------------
            elif msg.text in ["Raisaaa"]:
                ki.sendText(msg.to,"Apa sih manggil manggil, SKSD banget.􏿿")
#-----------------------------------------------
            elif msg.text in ["Ya makanya itu mau lebih deket"]:
                ki.sendText(msg.to,"Dih jijik.􏿿")
#-----------------------------------------------
            elif msg.text in ["Udah punya pacar belum?"]:
                ki.sendText(msg.to,"Udah.􏿿")
#-----------------------------------------------
            elif msg.text in ["Siapa namanya?"]:
                ki.sendText(msg.to,"Kepo banget sih.􏿿")
#-----------------------------------------------
            elif msg.text in ["Udah makan?"]:
                ki.sendText(msg.to,"Siapa lu nyuruh nyuruh gua?􏿿")
#-----------------------------------------------
            elif msg.text in ["Wi galak amat"]:
                ki.sendText(msg.to,"Terserah gua dong􏿿")
#-----------------------------------------------
            elif msg.text in ["Bisa ketemuan ga?"]:
                ki.sendText(msg.to,"Gak. Males banget ketemuan sama orang kaya Lo.􏿿")
#-----------------------------------------------
            elif msg.text in ["Dih"]:
                ki.sendText(msg.to,"Apa Lo?􏿿")
#-----------------------------------------------
            elif msg.text in ["Males ah jutek"]:
                ki.sendText(msg.to,"Ya udah tau jutek. ngapain masih ngechat?")
#-----------------------------------------------
            elif msg.text in ["Dah"]:
                ki.sendText(msg.to,"Sana pergi yang jauh.")
#-----------------------------------------------
            elif msg.text in ["Eh kita pacaran udah berapa lama?"]:
                if msg.from_ in admin:
                    ki.sendText(msg.to,"Udah 1 tahun lebih kalau ga salah..")
#-----------------------------------------------
            elif msg.text in ["Sayang","Raisa","Yaya","Beb"]:
                if msg.from_ in admin:
                    ki.sendText(msg.to,"Iya ada apa sayang?")
#-----------------------------------------------
            elif msg.text in ["Lagi apa?"]:
                if msg.from_ in admin:
                    ki.sendText(msg.to,"Lagi liatin foto kamu")
#-----------------------------------------------
            elif msg.text in ["Udah sholat?"]:
                if msg.from_ in admin:
                    ki.sendText(msg.to,"Udah dongg.. kamu gimana?")
#-----------------------------------------------
            elif msg.text in ["Aku udah juga"]:
                if msg.from_ in admin:
                    ki.sendText(msg.to,"Ohh okee baguslaa")
#-----------------------------------------------
            elif msg.text in ["We"]:
                if msg.from_ in admin:
                    ki.sendText(msg.to,"Are")
#-----------------------------------------------
            elif msg.text in ["One"]:
                if msg.from_ in admin:
                    ki.sendText(msg.to,"Love💕")
#-----------------------------------------------
            elif msg.text in ["Udah makan belum?"]:
                if msg.from_ in admin:
                    ki.sendText(msg.to,"Udah sayang...")
#-----------------------------------------------
            elif msg.text in ["Kenapa sayang?"]:
                if msg.from_ in admin:
                    ki.sendText(msg.to,"Gak tau tuh mereka berisik banget. Kesel akunya.")
#-----------------------------------------------
#--------------------------------------------------------speed
            elif msg.text in ["Ban:on"]:
                wait["wblacklist"] = True
                cl.sendText(msg.to,"Send Contact")
            elif msg.text in ["Unban:on"]:
                wait["dblacklist"] = True
                cl.sendText(msg.to,"Send Contact")
            elif msg.text.lower() == 'Mcheck':
                if wait["blacklist"] == {}:
                    cl.sendText(msg.to,"􀜁􀇔􏿿 Nothing in the blacklist")
                else:
                    cl.sendText(msg.to,"􀜁􀇔􏿿 following is a blacklist")
                    kontak = cl.getContacts(blacklist)
                num=1
                msgs="User Black List\n"
                for ids in kontak:
                    msgs+="\n%i. %s" % (num, ids.displayName)
                    num=(num+1)
                msgs+="\n\nTotal %i blacklist user(s)" % len(kontak)
                cl.sendText(msg.to, msgs)
                    #mc = ""
                    #for mi_d in wait["blacklist"]:
                        #mc += "�" +cl.getContact(mi_d).displayName + "\n"
                    #cl.sendText(msg.to,mc)                    
            elif msg.text.lower() == 'clear ban':
                wait["blacklist"] = {}
                cl.sendText(msg.to,"ヽ( ^ω^)ﾉ Unbanned Success")

            elif msg.text in ["Banlist"]:
                if wait["blacklist"] == {}:
                    cl.sendText(msg.to,"Nothing")
                else:
                    cl.sendText(msg.to,"Blacklist user")
                    mc = "✃┈┈[Blacklist]┈┈✍\n"
                    for mi_d in wait["blacklist"]:
                        mc += "[✗] " + cl.getContact(mi_d).displayName + " \n"
                    cl.sendText(msg.to, mc + "")
            elif msg.text in ["Ban cek","Cekban"]:
                if msg.toType == 2:
                    group = cl.getGroup(msg.to)
                    gMembMids = [contact.mid for contact in group.members]
                    matched_list = []
                    for tag in wait["blacklist"]:
                        matched_list+=filter(lambda str: str == tag, gMembMids)
                    cocoa = "✃┈[Blacklist]┈✍"
                    for mm in matched_list:
                        cocoa += "\n" + mm + "\n"
                    cl.sendText(msg.to, cocoa + "")
            elif msg.text in ["Kill ban"]:
                if msg.toType == 2:
                    group = cl.getGroup(msg.to)
                    gMembMids = [contact.mid for contact in group.members]
                    matched_list = []
                    for tag in wait["blacklist"]:
                        matched_list+=filter(lambda str: str == tag, gMembMids)
                    if matched_list == []:
                        cl.sendText(msg.to,"There was no blacklist user")
                        return
                    for jj in matched_list:
                        cl.kickoutFromGroup(msg.to,[jj])
                    cl.sendText(msg.to,"Blacklist user")
            elif msg.text in ["Kill"]:
                if msg.toType == 2:
                    group = ki.getGroup(msg.to)
                    gMembMids = [contact.mid for contact in group.members]
                    matched_list = []
                    for tag in wait["blacklist"]:
                        matched_list+=filter(lambda str: str == tag, gMembMids)
                    if matched_list == []:
                        ki.sendText(msg.to,"Daftar hitam pengguna tidak memiliki")
                        return
                    for jj in matched_list:
                        try:
                            cl.kickoutFromGroup(msg.to,[jj])
                            ki.kickoutFromGroup(msg.to,[jj])
                            ki2.kickoutFromGroup(msg.to,[jj])
                            ki3.kickoutFromGroup(msg.to,[jj])
                            ki4.kickoutFromGroup(msg.to,[jj])
                            ki5.kickoutFromGroup(msg.to,[jj])
                            ki6.kickoutFromGroup(msg.to,[jj])
                            print (msg.to,[jj])
                        except:
                            pass
            elif msg.text in ["Cancel"]:
                if msg.toType == 2:
                    group = cl.getGroup(msg.to)
                    gMembMids = [contact.mid for contact in group.invitee]
                    for _mid in gMembMids:
                        cl.cancelGroupInvitation(msg.to,[_mid])
                    cl.sendText(msg.to,"I pretended to cancel and canceled👈")
            elif "Album" in msg.text:
                try:
                    albumtags = msg.text.replace("Album","")
                    gid = albumtags[:33]
                    name = albumtags.replace(albumtags[:34],"")
                    cl.createAlbum(gid,name)
                    cl.sendText(msg.to,name + "We created an album👈")
                except:
                    cl.sendText(msg.to,"Error")
            elif "Fakecat’" in msg.text:
                try:
                    source_str = 'abcdefghijklmnopqrstuvwxyz1234567890@:;./_][!&amp;%$#)(=~^|'
                    name = "".join([random.choice(source_str) for x in xrange(10)])
                    amid = msg.text.replace("fakecâ†’","")
                    cl.sendText(msg.to,str(cl.channel.createAlbumF(msg.to,name,amid)))
                except Exception as e:
                    try:
                        cl.sendText(msg.to,str(e))
                    except:
                        pass
#-----------------------------------------------
            elif msg.text in ["Masuk"]:
                        G = cl.getGroup(msg.to)
                        ginfo = cl.getGroup(msg.to)
                        G.preventJoinByTicket = False
                        cl.updateGroup(G)
                        invsend = 0
                        Ticket = cl.reissueGroupTicket(msg.to)
                        ki.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.01)
                        #ki.sendText(msg.to,"􀜁􀇔Hello🙌 "  +  str(ginfo.name)  + "")
                        ki2.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.01)
                        #ki2.sendText(msg.to,"􀜁􀇔Hello🙌 "  +  str(ginfo.name)  + "")
                        ki3.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.01)
                       # ki3.sendText(msg.to,"􀜁􀇔Hello🙌 "  +  str(ginfo.name)  + "")
                        ki4.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.01)
                        #ki4.sendText(msg.to,"􀜁􀇔Hello🙌 "  +  str(ginfo.name)  + "")
                        ki5.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.01)
                       # ki5.sendText(msg.to,"􀜁􀇔Hello🙌 "  +  str(ginfo.name)  + "")
                        ki6.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.01)
                       # ki6.sendText(msg.to,"􀜁??Hello?? "  +  str(ginfo.name)  + "")
                         ki7.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.01)
                       # ki7.sendText(msg.to,"􀜁??Hello?? "  +  str(ginfo.name)  + "")
                        G = cl.getGroup(msg.to)
                        G.preventJoinByTicket = True
                        ki2.updateGroup(G)
                        print "kickers_Ok"
                        G.preventJoinByTicket(G)
                        ki.updateGroup(G)
#-----------------------------------------------
            elif "Sbye" in msg.text:
                if msg.toType == 2:
                    ginfo = cl.getGroup(msg.to)
                    try:
                        ki.sendText(msg.to,"􀜁􀇔􏿿Bye Bye😘 "  +  str(ginfo.name)  + "")
                        ki.leaveGroup(msg.to)
                      #  ki2.sendText(msg.to,"􀜁􀇔􏿿Bye Bye😘 "  +  str(ginfo.name)  + "")
                        ki2.leaveGroup(msg.to)
                     #   ki3.sendText(msg.to,"􀜁􀇔􏿿Bye Bye😘 "  +  str(ginfo.name)  + "")
                        ki3.leaveGroup(msg.to)
                     #   ki4.sendText(msg.to,"􀜁􀇔􏿿Bye Bye😘 "  +  str(ginfo.name)  + "")
                        ki4.leaveGroup(msg.to)
                     #   ki5.sendText(msg.to,"􀜁􀇔􏿿Bye Bye😘 "  +  str(ginfo.name)  + "")
                        ki5.leaveGroup(msg.to)
                     #   ki6.sendText(msg.to,"􀜁􀇔􏿿Bye Bye😘 "  +  str(ginfo.name)  + "")
                        ki6.leaveGroup(msg.to)
                     #   ki7.sendText(msg.to,"􀜁􀇔􏿿Bye Bye😘 "  +  str(ginfo.name)  + "")
                        ki7.leaveGroup(msg.to)
                    except:
                        pass
#-----------------------------------------------
            elif msg.text in ["Ry bye","Papay"]:
                if msg.toType == 2:
                    ginfo = cl.getGroup(msg.to)
                    try:
                        cl.sendText(msg.to,"􀜁􀇔􏿿Bye Bye😘 "  +  str(ginfo.name)  + "")
                        cl.leaveGroup(msg.to)
                    except:
                        pass

        #-------------Fungsi Broadcast Start------------#
            elif "Bc: " in msg.text:
				bctxt = msg.text.replace("Anu: ","")
				ki.sendText(msg.to,(bctxt))
				ki2.sendText(msg.to,(bctxt))
				ki3.sendText(msg.to,(bctxt))
				ki4.sendText(msg.to,(bctxt))
				k5.sendText(msg.to,(bctxt))
				ki6.sendText(msg.to,(bctxt))
       #--------------Fungsi Broadcast Finish-----------#

#-----------------------------------------------
            elif msg.text in ["Welcome","Wc"]:
                  ginfo = cl.getGroup(msg.to)
                  cl.sendText(msg.to,"Selamat Datang Di Grup " + str(ginfo.name))
                  #cl.sendText(msg.to,"Owner Grup " + str(ginfo.name) + " :\n" + ginfo.creator.displayName )
            elif "Say " in msg.text:
				  bctxt = msg.text.replace("Say ","")
				  ki.sendText(msg.to,(bctxt))
				  ki2.sendText(msg.to,(bctxt))
				  ki3.sendText(msg.to,(bctxt))
				  ki4.sendText(msg.to,(bctxt))
				  ki5.sendText(msg.to,(bctxt))
				  ki6.sendText(msg.to,(bctxt))
            elif msg.text in 'Ping':
                  ki.sendText(msg.to,"Ping 􀜁􀇔􏿿")
                  ki2.sendText(msg.to,"Ping 􀜁􀇔􏿿")
                  ki3.sendText(msg.to,"Ping 􀜁􀇔􏿿")
                  ki4.sendText(msg.to,"Ping 􀜁􀇔􏿿")
                  ki5.sendText(msg.to,"Ping 􀜁􀇔􏿿")
                  ki6.sendText(msg.to,"Ping 􀜁􀇔􏿿")
            elif "Spam " in msg.text:
              if msg.from_ in Bots or staff:
                txt = msg.text.split(" ")
                jmlh = int(txt[2])
                teks = msg.text.replace("Spam "+str(txt[1])+" "+str(jmlh)+ " ","")
                tulisan = jmlh * (teks+"\n")
                 #Keke cantik <3
                if txt[1] == "on":
                    if jmlh <= 60:
                       for x in range(jmlh):
                           cl.sendText(msg.to, teks)
                    else:
                       cl.sendText(msg.to, "Kelebihan batas:v")
                elif txt[1] == "off":
                    if jmlh <= 100:
                        cl.sendText(msg.to, tulisan)
                    else:
                        cl.sendText(msg.to, "Kelebihan batas :v")
            elif msg.text in ["Sp"]:
            	if msg.from_ in Bots or staff:
                  start = time.time()
                  cl.sendText(msg.to, "Wait...")
                  elapsed_time = time.time() - start
                  cl.sendText(msg.to, "%sseconds 􀨁􀄻double thumbs up􏿿" % (elapsed_time))
            elif msg.text in ["Speed"]:
            	if msg.from_ in Bots or staff:
                  start = time.time()
                  cl.sendText(msg.to, "Progress...")
                  elapsed_time = time.time() - start
                  cl.sendText(msg.to, "%s second" % (elapsed_time))
                  ki.sendText(msg.to, "%s second" % (elapsed_time))
                  ki2.sendText(msg.to, "%s second" % (elapsed_time))
                  ki3.sendText(msg.to, "%s second" % (elapsed_time))
                  ki4.sendText(msg.to, "%s second" % (elapsed_time))
                  ki5.sendText(msg.to, "%s second" % (elapsed_time))
                  ki6.sendText(msg.to, "%s second" % (elapsed_time))
#----------------------------------------------- 
            elif msg.text in ["Serk support"]:
                    msg.contentType = 13
                    msg.contentMetadata = {'mid': "u8ff494ceaf9c45b14c90f468ea6465be"}
                    ki.sendText(msg.to,"MySupport")
                    kk.sendText(msg.to,"Jangan Lupa Di Add Ya!!!")
                    ki.sendMessage(msg)
                    msg.contentType = 13
                    msg.contentMetadata = {'mid': "uc85fb100ee443a04974a44a84f7e550f"}
                    ki.sendText(msg.to,"MySupport")
                    kk.sendText(msg.to,"Jangan Lupa Di Add Ya!!!")
                    ki.sendMessage(msg)
                    msg.contentType = 13
                    msg.contentMetadata = {'mid': "ud8908cebb93df5fda9ee08920ae8693d"}
                    ki.sendText(msg.to,"MySupport")
                    kk.sendText(msg.to,"Jangan Lupa Di Add Ya!!!")
                    ki.sendMessage(msg)
#----------------------------------------------- 
#------------------------------------------------------------------
            elif msg.text in ["single"]:
                if msg.toType == 2:
                    group = cl.getGroup(msg.to)
                    gMembMids = [contact.mid for contact in group.invitee]
                    for _mid in gMembMids:
                        cl.cancelGroupInvitation(msg.to,[_mid])
                    cl.sendText(msg.to,"I have feigned and have canceled it。")
            elif "random:" in msg.text:
                if msg.toType == 2:
                    strnum = msg.text.replace("random:","")
                    source_str = 'abcdefghijklmnopqrstuvwxyz1234567890@:;./_][!&%$#)(=~^|'
                    try:
                        num = int(strnum)
                        group = cl.getGroup(msg.to)
                        for var in range(0,num):
                            name = "".join([random.choice(source_str) for x in xrange(10)])
                            time.sleep(0.01)
                            group.name = name
                            cl.updateGroup(group)
                    except:
                        cl.sendText(msg.to,"ЄƦƦƠƦ")
            elif "Album making" in msg.text:
                try:
                    albumtags = msg.text.replace("Album making","")
                    gid = albumtags[:33]
                    name = albumtags.replace(albumtags[:34],"")
                    cl.createAlbum(gid,name)
                    cl.sendText(msg.to,name + "An album was made。")
                except:
                    cl.sendText(msg.to,"ЄƦƦƠƦ")
            elif "fakec→" in msg.text:
                try:
                    source_str = 'abcdefghijklmnopqrstuvwxyz1234567890@:;./_][!&%$#)(=~^|'
                    name = "".join([random.choice(source_str) for x in xrange(10)])
                    amid = msg.text.replace("fakec→","")
                    cl.sendText(msg.to,str(cl.channel.createAlbumF(msg.to,name,amid)))
                except Exception as e:
                    try:
                        cl.sendText(msg.to,str(e))
                    except:
                        pass                
#-----------------------------------------------
#-----------------------------------------------             
            elif "Cleanse" == msg.text:
                if msg.from_ in admin:
                    if msg.toType == 2:
                        print "Kick all member"
                        _name = msg.text.replace("Cleanse","")
                        gs = ki.getGroup(msg.to)
                        gs = kk.getGroup(msg.to)
                        gs = kc.getGroup(msg.to)
                        ki.sendText(msg.to,"Sampai jumpaa~")
                        kc.sendText(msg.to,"Dadaaah~")
                        targets = []
                        for g in gs.members:
                            if _name in g.displayName:
                                targets.append(g.mid)
                        if targets == []:
                            ki.sendText(msg.to,"Not found.")
                            kk.sendText(msg.to,"Not found.")
                            kc.sendText(msg.to,"Not found.")
                        else:
                            for target in targets:
                                if target not in admin:
                                    try:
                                        klist=[ki,kk,kc]
                                        kicker=random.choice(klist)
                                        kicker.kickoutFromGroup(msg.to,[target])
                                        print (msg.to,[g.mid])
                                    except Exception as e:
                                        cl.sendText(msg.to,str(e))
                                        cl.inviteIntoGroup(msg.to, targets)
#--------------------------------------------------------
#Restart_Program
        elif msg.text in ["Bot:restart"]:
            if msg.from_ in Creator:
                cl.sendText(msg.to, "Bot has been restarted")
                restart_program()
                print "@Restart"
            else:
               cl.sendText(msg.to, "No Access")
#--------------------------------------------------------
            elif msg.text in "Tagall","Cipok semua":
                  group = cl.getGroup(msg.to)
                  nama = [contact.mid for contact in group.members]

                  cb = ""
                  cb2 = ""
                  strt = int(0)
                  akh = int(0)
                  for md in nama:
                      akh = akh + int(6)

                      cb += """{"S":"""+json.dumps(str(strt))+""","E":"""+json.dumps(str(akh))+""","M":"""+json.dumps(md)+"},"""

                      strt = strt + int(7)
                      akh = akh + 1
                      cb2 += "@nrik \n"

                  cb = (cb[:int(len(cb)-1)])
                  msg.contentType = 0
                  msg.text = cb2
                  msg.contentMetadata ={'MENTION':'{"MENTIONEES":['+cb+']}','EMTVER':'4'}

                  try:
                      cl.sendMessage(msg)
                  except Exception as error:
                      print error
#-----------------------------------------------
            elif msg.text in ["Ats@"]:
                  group = cl.getGroup(msg.to)
                  nama = [contact.mid for contact in group.members]

                  cb = ""
                  cb2 = ""
                  strt = int(0)
                  akh = int(0)
                  for md in nama:
                      akh = akh + int(6)

                      cb += """{"S":"""+json.dumps(str(strt))+""","E":"""+json.dumps(str(akh))+""","M":"""+json.dumps(md)+"},"""

                      strt = strt + int(7)
                      akh = akh + 1
                      cb2 += "@nrik \n"

                  cb = (cb[:int(len(cb)-1)])
                  msg.contentType = 0
                  msg.text = cb2
                  msg.contentMetadata ={'MENTION':'{"MENTIONEES":['+cb+']}','EMTVER':'4'}

                  try:
                      ki.sendMessage(msg)
                  except Exception as error:
                      print error
#-----------------------------------------------
        if op.type == 19:
                if op.param3 in Bots:
                    wait["blacklist"][op.param2] = True
                    
        if op.type == 19:
            if wait["MProtection"] == True:
                if op.param2 not in Bots:
                    ki4.kickoutFromGroup(op.param1,[op.param2])
                if op.param2 in wait["blacklist"]:
                    pass
                #if op.param2 in wait["whitelist"]:
                    #pass
                else:
                    wait["blacklist"][op.param2] = True
                    
        if op.type == 19:
                if not op.param2 in Bots:
                    try:
                        gs = ki.getGroup(op.param1)
                        gs = ki2.getGroup(op.param1)
                        gs = ki3.getGroup(op.param1)
                        gs = ki4.getGroup(op.param1)
                        gs = ki5.getGroup(op.param1)
                        gs = ki6.getGroup(op.param1)
                        targets = [op.param2]
                        for target in targets:
                           try:
                                wait["blacklist"][target] = True
                                f=codecs.open('st2__b.json','w','utf-8')
                                json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                           except:
                            pass
                                
                    except Exception, e:
                        print e
                if not op.param2 in Bots:
                  if wait["Backup"] == True:
                    try:
                        klist=[cl.ki,ki2,ki3,ki4,ki5,ki6]
                        kicker = random.choice(klist)
                        kicker.inviteIntoGroup(op.param1, [op.param3])
                    except Exception, e:
                        print e
                #if not op.param2 in Bots:
                  #if wait["protect"] == True:  
                   #try:
                       #klist=[ki.ki2.ki3.ki4.ki5.ki6]
                       #kicker = random.choice(klist)
                       #G = kicker.getGroup(op.param1)
                       #G.preventJoinByTicket = False
                       #kicker.updateGroup(G)
                       #invsend = 0
                       #Ticket = kicker.reissueGroupTicket(op.param1)
                       #ki7.acceptGroupInvitationByTicket(op.param1,Ticket)
                       #X = kicker.getGroup(op.param1)             
                       #X.preventJoinByTicket = True
                       #ki7.kickoutFromGroup(op.param1,[op.param2])
                       #kicker.kickoutFromGroup(op.param1,[op.param2])
                       #kicker.updateGroup(X)
                       #ki7.leaveGroup(op.param1)
                   #except Exception, e:
                            #print e
#-----------------------------------------------                         
        if op.type == 19:
            try:
                if op.param3 in mid:
                    if op.param2 in kimid:
                        G = ki.getGroup(op.param1)
                        G.preventJoinByTicket = False
                        ki.updateGroup(G)
                        Ticket = ki.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        cl.updateGroup(G)
                    else:
                        G = ki.getGroup(op.param1)
                        
                        ki.kickoutFromGroup(op.param1,[op.param2])

                        G.preventJoinByTicket = False
                        ki.updateGroup(G)
                        Ticket = ki.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        cl.updateGroup(G)
                        #ki.updateGroup(G)
                        wait["blacklist"][op.param2] = True

                elif op.param3 in kimid:
                    if op.param2 in ki2mid:
                        G = ki2.getGroup(op.param1)
                        G.preventJoinByTicket = False
                        ki2.updateGroup(G)
                        Ticket = ki2.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        ki2.updateGroup(G)
                    else:
                        G = ki2.getGroup(op.param1)


                        ki2.kickoutFromGroup(op.param1,[op.param2])

                        G.preventJoinByTicket = False
                        ki2.updateGroup(G)
                        Ticket = ki2.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        ki.updateGroup(G)

                elif op.param3 in ki3mid:
                    if op.param2 in ki2mid:
                        G = ki2.getGroup(op.param1)
                        G.preventJoinByTicket = False
                        ki2.updateGroup(G)
                        Ticket = ki2.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        ki2.updateGroup(G)
                    else:
                        G = cl.getGroup(op.param1)

                        
                        ki2.kickoutFromGroup(op.param1,[op.param2])

                        G.preventJoinByTicket = False
                        ki2.updateGroup(G)
                        Ticket = ki2.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        ki2.updateGroup(G)
                        
                elif op.param3 in ki2mid:
                    if op.param2 in ki3mid:
                        G = ki3.getGroup(op.param1)
                        G.preventJoinByTicket = False
                        ki3.updateGroup(G)
                        Ticket = ki3.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        ki3.updateGroup(G)
                    else:
                        G = ki3.getGroup(op.param1)

                        
                        ki3.kickoutFromGroup(op.param1,[op.param2])

                        G.preventJoinByTicket = False
                        ki3.updateGroup(G)
                        Ticket = ki3.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        ki3.updateGroup(G)
                        
                elif op.param3 in ki4mid:
                    if op.param2 in ki5mid:
                        G = ki5.getGroup(op.param1)
                        G.preventJoinByTicket = False
                        ki5.updateGroup(G)
                        Ticket = ki5.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        cl.updateGroup(G)
                    else:
                        G = ki5.getGroup(op.param1)

                        
                        ki5.kickoutFromGroup(op.param1,[op.param2])

                        G.preventJoinByTicket = False
                        ki5.updateGroup(G)
                        Ticket = ki5.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        ki5.updateGroup(G)

                elif op.param3 in ki5mid:
                    if op.param2 in ki4mid:
                        G = ki4.getGroup(op.param1)
                        G.preventJoinByTicket = False
                        ki4.updateGroup(G)
                        Ticket = ki4.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        ki4.updateGroup(G)
                    else:
                        G = ki4.getGroup(op.param1)

                        
                        ki4.kickoutFromGroup(op.param1,[op.param2])

                        G.preventJoinByTicket = False
                        ki4.updateGroup(G)
                        Ticket = ki4.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        ki4.updateGroup(G)

                elif op.param3 in ki6mid:
                    if op.param2 in ki5mid:
                        G = ki5.getGroup(op.param1)
                        G.preventJoinByTicket = False
                        ki5.updateGroup(G)
                        Ticket = ki5.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        ki5.updateGroup(G)
                    else:
                        G = ki5.getGroup(op.param1)

                        
                        ki5.kickoutFromGroup(op.param1,[op.param2])

                        G.preventJoinByTicket = False
                        ki5.updateGroup(G)
                        Ticket = ki5.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        ki5.updateGroup(G)
            except:
                pass
	if op.type == 17:
	    if op.param2 not in Bots:
		if op.param2 in Bots:
		    pass
	    if wait["protect"] == True:
		if wait["blacklist"][op.param2] == True:
		   try:
			random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
			G = random.choice(KAC).getGroup(op.param1)
			G.preventJoinByTicket = True
			ki.updateGroup(G)
#			random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
		   except:
#			pass
			try:
			    random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
			    G = random.choice(KAC).getGroup(op.param1)
			    G.preventJoinByTicket = True
			    random.choice(KAC).updateGroup(G)
#			    random.choice(KAK).kickoutFromGroup(op.param1,[op.param2])
			except:
			    pass
		elif op.param2 not in admin + Bots:
		    random.choice(KAC).sendText(op.param1,"Welcome. Don't Play Bots. I can kick you!")
	    else:
		pass
	if op.type == 19:
	    if op.param2 not in Bots:
		if op.param2 in Bots:
		    pass
		elif wait["protect"] == True:
		    wait ["blacklist"][op.param2] = True
		    random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
		else:
		    cl.sendText(op.param1,"")
	    else:
		cl.sendText(op.param1,"")
	if op.type == 13:
	    if op.param2 not in Bots:
		if op.param2 in Bots:
		    pass
		elif wait["inviteprotect"] == True:
		    wait ["blacklist"][op.param2] = True
		    ki2.kickoutFromGroup(op.param1,[op.param2])
		else:
		    ki2.sendText(op.param1,"")
	    else:
		ki2.sendText(op.param1,"")
	    if op.param2 not in Bots:
		if op.param2 in Bots:
		    pass
		elif wait["inviteprotect"] == True:
		    wait ["blacklist"][op.param2] = True
		    ki3.cancelGroupInvitation(op.param1,[op.param3])
		else:
		    ki3.sendText(op.param1,"")
	    else:
		ki3.sendText(op.param1,"")
	    if op.param2 not in Bots:
		if op.param2 in Bots:
		    pass
		elif wait["cancelprotect"] == True:
		    wait ["blacklist"][op.param2] = True
		    ki.cancelGroupInvitation(op.param1,[op.param3])
		else:
		    ki.sendText(op.param1,"")
	    else:
		ki.sendText(op.param1,"")
	if op.type == 11:
	    if op.param2 not in Bots:
		if op.param2 in Bots:
		    pass
		#elif wait["linkprotect"] == True:
		   # wait ["blacklist"][op.param2] = True
		    #G = ki.getGroup(op.param1)
		   # G.preventJoinByTicket = True
		  #  ki.updateGroup(G)
		  #  random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
		#else:
		  #  cl.sendText(op.param1,"")
	  #  else:
		#cl.sendText(op.param1,"")
        if op.type == 11:
            if wait["linkprotect"] == True:
                if op.param2 not in Bots:
                    G = ki.getGroup(op.param1)
                    G.preventJoinByTicket = True
                    Ticket = ki.reissueGroupTicket(op.param1)
                    ki7.acceptGroupInvitationByTicket(op.param1,Ticket)
                    ki7.kickoutFromGroup(op.param1,[op.param2])
                    ki.updateGroup(G)
                    ki7.leaveGroup(op.param1)
                    ki.senText(msg.to,"Please Dont open Qr")
                if op.param2 in wait["blacklist"]:
                    pass
                #if op.param2 in wait["whitelist"]:
                    #pass
                else:
                    wait["blacklist"][op.param2] = True
		#elif wait["linkprotect"] == True:
		    #wait ["blacklist"][op.param2] = True
		    #G = cl.getGroup(op.param1)
		    #G.preventJoinByTicket = False
		    #cl.updateGroup(G)
		    #Ticket = cl.reissueGroupTicket(op.param1)
		    #ki7.acceptGroupInvitationByTicket(op.param1,Ticket)
		    #X = cl.getGroup(op.param1)             
            #X.preventJoinByTicket = True
            #cl.updateGroup(X)
		    #ki7.kickoutFromGroup(op.param1,[op.param2])
		    #cl.updateGroup(X)
            #ki7.leaveGroup(op.param1)
		#else:
		    #cl.sendText(op.param1,"")
	    #else:
		#cl.sendText(op.param1,"")
        if op.type == 5:
            if wait["autoAdd"] == True:
                if (wait["message"] in [""," ","\n",None]):
                    pass
                else:
                    cl.sendText(op.param1,str(wait["message"]))

        if op.type == 59:
            print op


    except Exception as error:
        print error


def a2():
    now2 = datetime.now()
    nowT = datetime.strftime(now2,"%M")
    if nowT[14:] in ["10","20","30","40","50","00"]:
        return False
    else:
        return True
def nameUpdate():
    while True:
        try:
        while a2():
            pass
            if wait["clock"] == True:
                now2 = datetime.now()
                nowT = datetime.strftime(now2,"༺%H:%M༻")
                profile = cl.getProfile()
                profile.displayName = wait["cName"] + nowT
                cl.updateProfile(profile)
            time.sleep(600)
        except:
            pass
thread2 = threading.Thread(target=nameUpdate)
thread2.daemon = True
thread2.start()

def autolike():
    for zx in range(0,50):
        hasil = cl.activity(limit=1000)
        if hasil['result']['posts'][zx]['postInfo']['liked'] == False:
          try:    
            cl.like(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],likeType=1002)
            cl.comment(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],"Auto Like By ~SERK*TEAM~ \n\nLike Like LIke\n https://line.me/R/ti/p/~rd.rmdhn")
            ki.like(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],likeType=1002)
            ki.comment(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],"Auto Like By ~SERK*TEAM~ \n\nLike Like LIke\nId: line://line.me/R/ti/p/%40dlh6592k")
            ki2.like(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],likeType=1002)
            ki2.comment(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],"Auto Like By ~SERK*TEAM~ \n\nLike Like LIke\n https://line.me/R/ti/p/~rd.rmdhn")
            ki3.like(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],likeType=1002)
            ki3.comment(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],"Auto Like By ~SERK*TEAM~ \n\nLike Like LIke\nId: line://line.me/R/ti/p/%40qbs3336q")
            ki4.like(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],likeType=1002)
            ki4.comment(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],"Auto Like By ~SERK*TEAM~ \n\nLike Like LIke\n https://line.me/R/ti/p/~rd.rmdhn")
            ki5.like(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],likeType=1002)
            ki5.comment(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],"Auto Like By ~SERK*TEAM~ \n\nLike Like LIke\nId: line://line.me/R/ti/p/%40fss0252j")
            ki6.like(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],likeType=1002)
            ki6.comment(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],"Auto Like By ~SERK*TEAM~ \n\nLike Like LIke\n https://line.me/R/ti/p/~rd.rmdhn")
            ki7.ike(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],likeType=1002)
            ki7.comment(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],"Auto Like By ~SERK*TEAM~ \n\nLike Like LIke\nId: line://line.me/R/ti/p/%40vov9915v")
            print "Lagi Otw Nge-Like"
            print "Lagi Otw Nge-Like"
          except:
              pass
        else:
            print "Sudah DiLike Semua Kok"
            print "Sudah DiLike Semua Kok"

     time.sleep(600)
thread2 = threading.Thread(target=autolike)
thread2.daemon = True
thread2.start()
        if op.type == 59:
            print op


    except Exception as error:
        print error


def a2():
    now2 = datetime.now()
    nowT = datetime.strftime(now2,"%M")
    if nowT[14:] in ["10","20","30","40","50","00"]:
        return False
    else:
        return True
def nameUpdate():
    while True:
        try:
        while a2():
            pass
            if wait["clock"] == True:
                now2 = datetime.now()
                nowT = datetime.strftime(now2,"༺%H:%M༻")
                profile = cl.getProfile()
                profile.displayName = wait["cName"] + nowT
                cl.updateProfile(profile)
            time.sleep(600)
        except:
            pass
thread2 = threading.Thread(target=nameUpdate)
thread2.daemon = True
thread2.start()


while True:
    try:
        Ops = cl.fetchOps(cl.Poll.rev, 5)
    except EOFError:
        raise Exception("It might be wrong revision\n" + str(cl.Poll.rev))

    for Op in Ops:
        if (Op.type != OpType.END_OF_OPERATION):
            cl.Poll.rev = max(cl.Poll.rev, Op.revision)
            bot(Op)

