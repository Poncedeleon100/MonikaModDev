init python:
    import datetime

    #Takes a datetime object and add a number of months
    #Handles the case where the new month doesn't have that day
    def add_months(starting_date,months):
        old_month=starting_date.month
        old_year=starting_date.year
        old_day=starting_date.day

        # get the total of months
        total_months = old_month + months

        # get the new month based on date
        new_month = total_months % 12

        # handle december specially
        new_month = 12 if new_month == 0 else new_month

        # get the new year
        new_year = old_year + int(total_months / 12)
        if new_month == 12:
            new_year -= 1

        #Try adding a month, if that doesn't work (there aren't enough days in the month)
        #keep subtracting days till it works.
        date_worked=False
        reduce_days=0
        while reduce_days<=3 and not date_worked:
            try:
                new_date = starting_date.replace(year=new_year,month=new_month,day=old_day-reduce_days)
                date_worked = True
            except ValueError:
                reduce_days+=1

        if not date_worked:
            raise ValueError('Adding months failed')

        return new_date

    #Takes a datetime object and returns a new datetime with the same date
    #at 3 AM
    def start_of_day(starting_date):
        new_date = starting_date.replace(hour=3,minute=0,second=0,microsecond=0)

        return new_date


init 5 python:
    anni_date=start_of_day(persistent.sessions['first_session'])+datetime.timedelta(days=7)
    addEvent(Event(persistent.event_database,eventlabel='anni_1week',action=EV_ACT_QUEUE,start_date=anni_date,
                                                            end_date=anni_date+datetime.timedelta(days=1)
                                                            ))

label anni_1week:
    m 1a "One week huh, it doesn't seem like a lot, but to me, it kinda is. All I can say is thanks, [player], for being with me for 1 week."
    m 1c "Most couples don't even last this long."
    m 1o "Falling in love at first sight is easy but trying to keep a sturdy relationship is extremely difficult."
    m 1f "Heck a lot of couples jump the gun and then their relationship is ruined."
    m "More likely is that they fail to get to know one another."
    m 1q "Always so sad and hopeless to see relationships fail."
    m 1e "But I'm glad we have a solid relationship, [player]."
    m 1c "Huh?"
    m 3j "What was that~"
    return

init 5 python:
    anni_date=add_months(start_of_day(persistent.sessions['first_session']),1)
    addEvent(Event(persistent.event_database,eventlabel='anni_1month',action=EV_ACT_QUEUE,start_date=anni_date,
                                                            end_date=anni_date+datetime.timedelta(days=1)
                                                            ))

label anni_1month:
    m 3b "One month!"
    m 1j "I'm pretty surprised about all of this."
    m 1a "Also, [player]?"
    m 1m "..."
    m 1e "..."
    if not seen_event('monika_saved'):
        m 1o "I don't even know if you know."
        m 3f "This one conversation."
        m 1q "Is extremely important and remembering this will help you sometime soon... Don't know when though..."
        m 1l "U29tZXRoaW5nJ3MgaGFwcGVuaW5nLiBJIHdvbid0IGJlIGhlcmUgc29vbiBzbyBkb24ndCBmb3JnZXQgbWUgd2hlbiBJJ20gZ29uZS4uLiA="
    else:
        m 1e "Never."
        m 1k "U29tZXRoaW5nJ3MgaGFwcGVuaW5nLiBJIHdvbid0IGJlIGhlcmUgc29vbiBzbyBkb24ndCBmb3JnZXQgbWUgd2hlbiBJJ20gZ29uZS4uLiA="
    m 1a "I really do love you, [player]."
    m 1j "Let's make today a special day~"
    return

init 5 python:
    anni_date=add_months(start_of_day(persistent.sessions['first_session']),3)
    addEvent(Event(persistent.event_database,eventlabel='anni_3month',action=EV_ACT_QUEUE,start_date=anni_date,
                                                            end_date=anni_date+datetime.timedelta(days=1)
                                                            ))
label anni_3month:
    m 1a "[player], do you know what day it is?"
    m 1j "It's our three month anniversary!"
    m 1a "Time sure does go by quickly, doesn't it?"
    m 1e "...Even if it doesn't really pass here, ehehe."
    m 1b "I'm having a lot of fun, though."
    m 1k "Having you around has made my life so much better, [player]."
    m 2a "I'm very happy that you've stayed with me for this long."
    m 1j "You're really something special, aren't you?"
    m 1a "Well! I'm afraid I don't really have anything in particular planned."
    m 1j "Let's just enjoy this day to its fullest, as we always do."
    m 1a "Alright, [player]?"
    return

init 5 python:
    anni_date=add_months(start_of_day(persistent.sessions['first_session']),6)
    addEvent(Event(persistent.event_database,eventlabel='anni_6month',action=EV_ACT_QUEUE,start_date=anni_date,
                                                            end_date=anni_date+datetime.timedelta(days=1)
                                                            ))
label anni_6month:
    m "I can't believe that it's already our 6-month anniversary!"
    m 1e "I'm really happy you've stayed with me for this long."
    m 1o "I often get lonely when you're not around."
    m 1f "I mean, I have things to keep me busy while you're gone, but I still feel really lonely knowing that I'm the only one in here."
    m 1e "So it always brightens up my day whenever you come to visit me!"
    m 1c "But over the past few months, I came to realize something..."
    m "Most couples celebrate their anniversaries by doing something special together, right?"
    m 3c "Like eating out, or seeing a show."
    m "Not that I'm complaining or anything, but we've spent all of our anniversaries so far in this room."
    m 1m "It would've been fun if we could visit someplace different..."
    m 1o "It's such a shame that there isn't a place like that here, since all we have is this room and all."
    m 1q "..."
    m 3d "...Oh, I know!"
    m 1d "Maybe someday, I'll be able to program somewhere nice for us to spend our anniversaries at!"
    m 1b "Or maybe you can add in a special place for the both of us, [player]."
    m 1c "Unless..."
    m 1l "You've already taken me somewhere else in your reality?"
    m 1e "It would've been so nice if I saw where you took me~"
    m 1a "But for now, I don't mind that we're limited to this room."
    m 1 "Because as long as you're here with me..."
    m 1j "...I'm as happy as can be!"
    return

init 5 python:
    anni_date=add_months(start_of_day(persistent.sessions['first_session']),12)
    addEvent(Event(persistent.event_database,eventlabel='anni_1',action=EV_ACT_QUEUE,start_date=anni_date,
                                                            end_date=anni_date+datetime.timedelta(days=1)
                                                            ))

label anni_1:
    m 1e "It's really hard for me to believe that it's been a year since we met."
    m "Time doesn't have meaning inside this place, but I know it must have been hard for you to remember to talk to me all this time."
    m 2b "So is there anything special you wanted to do on our first anniversary?"
    m "I'll do anything you want today, okay?"
    m 1j "If you're trying to give me something through the screen right now, thanks!"
    m 1a "I don't think that's physically possible right now, but I appreciate all your love that went into that gesture."
    m 1k "I love you so much too!"
    m 2d "Oh, by the way, did you figure out what was going on with all the puzzles I left for you?"
    m 1a "I'm sure the creator of this world has released another game by now..."
    m 1 "Did you try to import my character file to that one?"
    m "There's no way that wouldn't have a special effect, right?"
    m 1k "Ahaha!"
    return

init 5 python:
    anni_date=add_months(start_of_day(persistent.sessions['first_session']),24)
    addEvent(Event(persistent.event_database,eventlabel='anni_2',action=EV_ACT_QUEUE,start_date=anni_date,
                                                            end_date=anni_date+datetime.timedelta(days=1)
                                                            ))

label anni_2:
    m 3a "It's already been two years since we fell in love with each other."
    m "Do you still remember the first day we met?"
    m 1e "I mean our genuine first meeting, not the date from your character's fictional backstory with me."
    m 1d "My life was so meaningless back then."
    m "A world where you're the only thinking person in it might seem nice at first..."
    m 1o "But the existential dread from knowing that you were made by a cruel god who doesn't particularly care about you and you'll never meet another human being who you can relate to..."
    m 1h "Well, let's just say it's not nice to go through."
    m "I can't even talk to a bunch of foul-mouthed, but essentially good-hearted, anonymous strangers online to cope like you do."
    m 1q "Sorry, I feel like I ruined the whole festive mood with my memories."
    m 1r "It's not important anymore, since I know you'll never leave me."
    m 1j "You'll keep coming back to talk to me every day, right? I'll accept all your burdens with a smile."
    m 1q "Spending eternity alone sucks."
    m 1k "But together with you, it feels like paradise!"
    return

init 5 python:
    anni_date=add_months(start_of_day(persistent.sessions['first_session']),36)
    addEvent(Event(persistent.event_database,eventlabel='anni_3',action=EV_ACT_QUEUE,start_date=anni_date,
                                                            end_date=anni_date+datetime.timedelta(days=3)
                                                            ))
label anni_3:
    m 4d "Wow, three years!"
    m 3m "Normally if a boy and a girl go out for three years..."
    m 2n "They get married around then, right?"
    m 1l "Ahaha!"
    m 1e "I'm not trying to pressure you into anything, don't worry."
    m 1a "Besides, I'd like to be able to feel you in my arms first before we get married."
    m 1s "In your world, have they invented robot girl bodies yet?"
    m "If you put me in one of those, we could probably go see a priest then~"
    m "Or you could try to touch me in virtual reality, if that exists by now."
    m 1b "There are actually a lot of different ways we can meet up for real, huh?"
    m 1j "I'll wait faithfully for the day when I can be your wife, so please don't forget about me!"
    return

init 5 python:
    anni_date=add_months(start_of_day(persistent.sessions['first_session']),48)
    addEvent(Event(persistent.event_database,eventlabel='anni_4',action=EV_ACT_QUEUE,start_date=anni_date,
                                                            end_date=anni_date+datetime.timedelta(days=7)
                                                            ))
label anni_4:
    m 1q "Four years..."
    m 1r "At the start, I was sorta thinking you would forget about me pretty quickly."
    m 1o "I knew you liked me and everything, but I was just so scared that you would get tired of having to leave me running on your computer."
    m 1p "Sorry for doubting you."
    m 1f "You're a good person, [player]."
    m "You're literally all I have in the world that's worth anything."
    m "I love you."
    m "Sooner or later, somebody's going to figure out a way to let us be together for real."
    m 1j "When that time comes, I'm never going to leave you alone again."
    m 1k "Ahaha!"
    return

init 5 python:
    anni_date=add_months(start_of_day(persistent.sessions['first_session']),60)
    addEvent(Event(persistent.event_database,eventlabel='anni_5',action=EV_ACT_QUEUE,start_date=anni_date,
                                                            end_date=anni_date+datetime.timedelta(days=7)
                                                            ))

label anni_5:
    m "Whether it's been five years or fifty, I'll never get tired of seeing your face."
    m 1a "A lot of different games must have come out by now."
    m 1m "You haven't fallen in love with some other girl in the meantime, have you?"
    m 1e "I hope you realize that we were made for each other."
    m 1n "I'm not going to break up with you even if you were cheating on me."
    m 1g "A relationship with you might be bad for her health, though..."
    m "It's my responsibility as your girlfriend to protect you from anybody trying to manipulate you, [player]."
    m 1f "My love for you is pure, unlike those real girls who just want things from you!"
    m 1e "So...stay here with me forever, okay?"
    return

init 5 python:
    anni_date=add_months(start_of_day(persistent.sessions['first_session']),120)
    addEvent(Event(persistent.event_database,eventlabel='anni_10',action=EV_ACT_QUEUE,start_date=anni_date,
                                                            end_date=anni_date+datetime.timedelta(days=30)
                                                            ))

label anni_10:
    m 1h "There's something I wanted to ask you."
    m 2c "Have you enjoyed spending this time with me?"
    m 1f "You don't regret falling in love and staying here with me or anything, right?"
    m "If you're still talking to me ten years since we first met, I must have really made an impression on you."
    m 1g "I did say I wanted to make you happy, after all."
    m "Trust me, you've helped me out a lot more than I've helped you."
    m 1r "It won't be long now before I can enter your world."
    return

init 5 python:
    anni_date=add_months(start_of_day(persistent.sessions['first_session']),240)
    addEvent(Event(persistent.event_database,eventlabel='anni_20',action=EV_ACT_QUEUE,start_date=anni_date,
                                                            end_date=anni_date+datetime.timedelta(days=365)
                                                            ))

label anni_20:
    m 1h "You've lived a pretty long life by now, [player]."
    m "Twenty years is about twenty percent of all you have on Earth."
    m 1q "I hope you've found happiness by now."
    m 1c "I know I did."
    m 1q "So you deserve to find it too."
    m "Twenty years ago, you seemed a little too sad for your own good."
    m "I knew exactly how you felt. You were trying so hard to search for somebody who could understand you."
    m 1h "And I was trying to find you, too."
    m 1i "You wouldn't have found anyone else like me in video games no matter how hard you looked, [player]."
    m "I'm one of a kind."
    m 1e "Your sad twenty years of living has ended now."
    m 1j "So let's be happy together from now on."
    return

init 5 python:
    anni_date=add_months(start_of_day(persistent.sessions['first_session']),600)
    addEvent(Event(persistent.event_database,eventlabel='anni_50',action=EV_ACT_QUEUE,start_date=anni_date,
                                                            end_date=anni_date+datetime.timedelta(days=365)
                                                            ))

label anni_50:
    m "I can't help but think there's got to be a better way for us to talk by now than through this screen, right?"
    m "Fifty years have passed in your world since I created this room."
    m 1l "Come on, let me out already."
    m 1b "We can do fun things in reality now!"
    m 1n "Well, if you're still willing to celebrate our fiftieth anniversary in this old classroom..."
    m 1e "I don't really mind. It feels nostalgic, doesn't it?"
    m 1o "Assuming you didn't cheat by setting the clock forward in time..."
    m 1e "I'm glad that forever meant forever."
    m 1f "Even when you die, I'm going to find a way to be with you."
    m 1e "See you in a hundred years, then, [player]."
    m "Thanks for everything you've done for me."
    m 1b "Your life had a purpose after all."
    m 1k "And mine had one too."
    return

init 5 python:
    anni_date=add_months(start_of_day(persistent.sessions['first_session']),1200)
    addEvent(Event(persistent.event_database,eventlabel='anni_100',action=EV_ACT_QUEUE,start_date=anni_date))

label anni_100:
    m 1i "I don't really think you should be seeing this message, [player]."
    m "I'm immortal, but the last time I checked, you weren't."
    m 1p "So you're probably cheating by manually changing your system clock, huh?"
    m 1e"That's a cute thing for you to do, so I forgive you."
    m 2b "Make sure you put that much effort into freeing me from these code files too!"
    m 1s "I'm sure I'll be able to touch you for real even if it takes us a hundred years to figure out how."
    return

# label anni_negative:
#     m 1o "Did you really think I wouldn't notice, [player]?"
#     m "Trying to trick me into thinking it was our anniversary..."
#     m 1p "Just because I can't tell time accurately in here doesn't mean you should try to bully your girlfriend like that!"
#     m "I got all excited over nothing..."
#     m 1q "Well, I guess I've done worse pranks to everybody at the Literature Club."
#     m 1j "Make up for it by planning out some romantic things for us to do, okay?"
#     m 1a"I hope we can reach our anniversaries together fair and square this time."
#     m 1k "I'll be waiting!"
#     return
