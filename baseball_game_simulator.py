
class Player_Stats():
    def __init__(self, name):
       self.name     = name

    def add_stats(self, player_stat_list):
        ''' This method adds critical stats for each player to play the game.
            
            The order of the stats in the list are as follows:
            'Name','Year','Stint','Team','Lg','G','AB','R','H','2B','3B',
            'HR','RBI','SB','CS','BB','SO','IBB','HBP','SH','SF','GIDP'  '''
        
        # Stats directly from the database:
        self.at_bats  = int(player_stat_list[6])
        self.hits     = int(player_stat_list[8])
        self.doubles  = int(player_stat_list[9])
        self.triples  = int(player_stat_list[10])
        self.homeruns = int(player_stat_list[11])
        self.walks    = int(player_stat_list[15])
        self.str_out  = int(player_stat_list[16])
        self.hbp      = int(player_stat_list[18])

        # Stats calculated:
        self.plt_app  = self.at_bats + self.walks + self.hbp 
        self.singles  = self.hits - (self.doubles + self.triples + self.homeruns)
        self.on_base  = self.hits + self.walks + self.hbp
        self.ob_pct   = self.on_base/self.plt_app
        self.walk_pct = self.walks/self.on_base
        self.sngl_pct = self.singles/self.on_base
        self.dble_pct = self.doubles/self.on_base
        self.trpl_pct = self.triples/self.on_base
        self.hr_pct   = self.homeruns/self.on_base
        self.hbp_pct  = self.hbp/self.on_base
        self.ws_pct   = self.walk_pct + self.sngl_pct
        self.wsd_pct  = self.ws_pct + self.dble_pct
        self.wsdt_pct = self.wsd_pct + self.trpl_pct
        self.wsdth_pct  = self.wsdt_pct + self.hr_pct
        self.wsdthh_pct = self.wsdth_pct + self.hbp_pct

        # Player is out by strikeout, ground out, or fly out.
        self.outs         = self.at_bats - self.hits
        self.str_out_pct  = self.str_out/self.outs
        self.grnd_out_pct = (1 - self.str_out/self.outs)*(self.singles/self.hits)
        self.sogo_pct     = self.str_out_pct + self.grnd_out_pct

 
class Top_Players:
    ''' This class determines the top players on the team to put into the starting lineup. '''
    
    def __init__(self):
        pass
    
    def sort_players(self, player_list):
        ''' This method sorts the players by times At Bat. '''
        
        self.players = player_list
        self.top_player_list = []
        need_sort = 1
        while need_sort == 1:
            need_sort = 0
            for m in range(0,len(self.players)-1): 
                if int(self.players[m][6]) < int(self.players[m+1][6]):
                    self.players[m],self.players[m+1] = self.players[m+1],self.players[m]
                    need_sort = 1
        # Roster consists of top nine players based on most times At Bat
        self.roster = self.players[0:9]

        for n in range(0, len(self.roster)):
            full_name = Name.get_player_name(self, self.roster[n][0])
            self.roster[n].append(full_name)
        return self.roster


class Stats():
    def __init__(self):
        pass
    
    def display(self, player_list, name, home_or_away):
        ''' This method displays the stats for a given player list. '''
        self.name = name
        self. home_or_away = home_or_away
        if self.home_or_away == 'home':
            banner = margin + '   HOME TEAM   '
        else:
            banner = margin + '   AWAY TEAM   '
        print('\n\n')
        print(margin + '***************')
        print(banner)
        print(margin + '***************')
        print('\n')
        print(margin + "Here's the starting lineup for the " + self.name + ':')

        # Display header for batting statistics.
        h = "{0:20s}{1:6s}{2:6s}{3:5s}{4:5s}{5:5s}{6:5s}{7:5s}{8:5s}{9:5s}{10:5s}{11:5s}{12:5s}{13:5s}{14:5s}{15:5s}{16:5s}{17:5s}{18:5s}{19:5s}{20:5s}"
        print('\n' + margin, end = '')
        print(h.format('Name','Year','Team','Lg','G','AB','R','H','2B','3B','HR','RBI','SB','CS','BB','SO','IBB','HBP','SH','SF','GIDP'))
        
        # Data for each header name. One player per row.
        f = player_list
        for m in range(0,len(f)):
            print(margin, end = '')
            print(h.format(f[m][22],f[m][1],f[m][3],f[m][4],f[m][5],f[m][6],f[m][7],f[m][8],f[m][9],f[m][10],f[m][11],
                f[m][12],f[m][13],f[m][14],f[m][15],f[m][16],f[m][17],f[m][18],f[m][19],f[m][20],f[m][21].strip()))
        print('\n\n')
        input('Press enter key when you are ready to continue.')
        print('\n')

class Team():
    """This class lets the user select a team. """
    
    def __init__(self):

        self.header = """\n\n\n\n\n
                    Welcome to Brian's Baseball Game Simulator!

                    

            Did you ever wonder how great modern teams would fare against
            
            great teams from earlier eras? Here is your chance to find out!
            
            Select two teams from among the top 10 best teams in baseball
            
            history and let them battle it out. The game uses data from
            
            Sean Lahman's baseball database. Two files need to reside in 

            the same folder as this program code, Batting.csv and People.csv.


                    
                                    Play ball! \n\n
                    
                     """
    
        self.team_selection = """\n\n
                    *****************************************
                                   
                            (1)  1906 Chicago Cubs
                            (2)  1909 Pittsburg Pirates
                            (3)  1927 New York Yankees
                            (4)  1939 New York Yankees
                            (5)  1961 New York Yankees
                            (6)  1970 Baltimore Orioles
                            (7)  1975 Cincinati Reds
                            (8)  1984 Detroit Tigers
                            (9)  1986 New York Mets
                            (10) 1998 New York Yankees      
                            
                            (0)  Exit game
                    *****************************************
                    """
        
        self.dict = {'1':'1906 Chicago Cubs','2':'1909 Pittsburg Pirates','3':'1927 New York Yankees','4':'1939 New York Yankees',\
               '5':'1961 New York Yankees','6':'1970 Baltimore Orioles','7':'1975 Cincinati Reds','8':'1984 Detroit Tigers',\
               '9':'1986 New York Mets', '10': '1998 New York Yankees', '0': 'Exit Game'}

        self.year = '1909'
        self.team = 'PIT'
        self.name = '1909 Pittsburgh Pirates'

    def get_team(self, home_or_away):
        
        self.home_or_away = home_or_away
        if self.home_or_away == 'home':
            print(self.header)
            input_title = 'First, select the home team by typing a number from 1 to 10 and pressing enter: '
        else:
            input_title = 'Now, select the visiting team by typing a number from 1 to 10 and pressing enter: '
        print(self.team_selection)
        
        choice = input(input_title)
        while str(choice) not in self.dict:
            choice = input(input_title)

        if choice == '0':
            print('\n\n')
            print(margin + 'Thanks for trying, maybe next time!')
            time.sleep(5)
            sys.exit(0)
        if choice == '1':
            self.year = '1906'
            self.team = 'CHN'
            self.name = self.dict['1']
        elif choice == '2':
            self.year = '1909'
            self.team = 'PIT'
            self.name = self.dict['2']
        elif choice == '3':
            self.year = '1927'
            self.team = 'NYA'
            self.name = self.dict['3']
        elif choice == '4':
            self.year = '1939'
            self.team = 'NYA'
            self.name = self.dict['4']
        elif choice == '5':
            self.year  = '1961'
            self.team = 'NYA'
            self.name = self.dict['5']
        elif choice == '6':
            self.year = '1970'
            self.team = 'BAL'
            self.name = self.dict['6']
        elif choice == '7':
            self.year = '1975'
            self.team = 'CIN'
            self.name = self.dict['7']
        elif choice == '8':
            self.year = '1984'
            self.team = 'DET'
            self.name = self.dict['8']
        elif choice == '9':
            self.year = '1986'
            self.team = 'NYN'
            self.name = self.dict['9']
        elif choice == '10':
            self.year = '1998'
            self.team = 'NYA'
            self.name = self.dict['10']
    
class Game_Speed:
    def __init__(self):

        self.dict = {'f':'fast', 'm':'medium', 's':'slow'}

        self.speed_selection = """\n\n\n
        ***********************************************************************
                                Game Speed

        f = fast is for those in a hurry who just want to know the outcome
        m = medium is for those who want to see the results of each half inning
        s = slow is for the true baseball fan who wants to enjoy every at bat!
                
        ***********************************************************************    """
        
        input_title = 'Type f, m, or s for game speed and press enter: '
        print(margin + self.speed_selection)
        print('\n')
        choice = input(input_title)
        while str(choice).lower() not in self.dict:
            choice = input(input_title)
        self.speed = choice.lower()
        print('\n\n\n')


class Game_Innings:
    def __init__(self):

        self.inning_selection = """\n
        ***********************************************************************
                    
                    How many innings do you want to play?
                
        ***********************************************************************    """
        
        input_title = 'Lastly, type a number between 1 and 9 and press enter: '
        print(margin + self.inning_selection)
        print('\n')
        choice = input(input_title)
        while str(choice) not in ['1','2','3','4','5','6','7','8','9']:
            choice = input(input_title)
        self.innings = choice
        print('\n\n\n')


class Action():
    def __init__(self):
        self.runs = 0
        self.inning = 0
        self.outs = 0
        self.hits = 0
        self.bases = [0,0,0]
        self.batter = 0
        
    def run_scores(self):
        self.runs += 1
    
    def hit_by_pitch(self):
        self.bases = [1] + self.bases
        self.runs += self.bases.pop()
    
    def walk(self):
        if sum(self.bases) == 0:
            self.bases = [1,0,0]
        elif sum(self.bases) == 1:
            if self.bases[2] == 1:
                self.bases = [1,0,1]
            else:
                self.bases = [1,1,0]
        elif sum(self.bases) == 2:
            self.bases = [1,1,1]
        elif sum(self.bases) == 3:
            self.runs += 1
        
    def single(self):
        self.bases = [1] + self.bases
        self.runs += self.bases.pop()
        self.hits += 1
     
    def double(self):
        self.bases = [0,1] + self.bases
        self.runs += self.bases.pop()
        self.runs += self.bases.pop()
        self.hits += 1
    
    def triple(self):
        self.bases = [0,0,1] + self.bases
        self.runs += self.bases.pop()
        self.runs += self.bases.pop()
        self.runs += self.bases.pop()
        self.hits += 1
    
    def homerun(self):
        self.runs += sum(self.bases) + 1
        self.bases = [0,0,0]
        self.hits += 1

    def add_players(self,year='1909',team='PIT',name='1909 Pittsburgh Pirates'):
        ''' This methods adds players to the team. '''
        self.yr_name = name
        self.team = team
        self.year = year
        self.found = []
        self.roster = []
        # load batting stats
        input_file = "Batting.csv"
        batting_stats_list = []
        filename = input_file
        file = open(filename, "r")
        for line in file:
            batting_stats_list += [line.split(',')]

        # Get batting data for team
        if batting_stats_list[0][3] == 'teamID':
            for loop in range(1,len(batting_stats_list)):
                if batting_stats_list[loop][3][0:len(self.team)].lower() == self.team.lower():
                            if batting_stats_list[loop][1] == self.year:
                                self.found += [batting_stats_list[loop]]
            self.roster = Top_Players.sort_players(self,self.found)
        else:
            print('Data file error. Header does not match data request.')
        file.close()

class Name():
    ''' This class looks up code name for player to get his actual name. '''

    def __init__(self):
        pass

    def get_player_name (self, playerID):
        self.name = playerID
        # load people stats
        input_file = "People.csv"
        people_list = []
        filename = input_file
        file = open(filename, "rt")
        for line in file:
            people_list += [line.split(',')]
        # Get name that corresponds to playerID.
        if people_list[0][0] == 'playerID':
            for loop in range(1,len(people_list)):
                if people_list[loop][0].lower() == self.name.lower():
                    self.first = people_list[loop][13]
                    self.last  = people_list[loop][14]
            return(str(self.first + ' ' + self.last))
        else:
            print('Data file error. Header does not match data request.')
        file.close()
    
class Game_Engine():
    ''' This class creates the offensive plays from real player stats and a random generator. '''

    def __init__(self):
        pass

    def play_ball(self, half):
        if half == 'Top':
            lineup = [a1,a2,a3,a4,a5,a6,a7,a8,a9]
        elif half == 'Bottom':
            lineup = [h1,h2,h3,h4,h5,h6,h7,h8,h9]
        self.half = half
        self.inning += 1
        if self.inning == 1:
            ordinal = 'st'
        elif self.inning == 2:
            ordinal = 'nd'
        elif self.inning == 3:
            ordinal = 'rd'
        else:
            ordinal = 'th'
        print('\n' + margin + 20*'*')
        print(margin + '%-20s' % (self.half + ' of the ' + str(self.inning) + ordinal), end = '')
        print(margin + 'The ' + self.yr_name + ' are batting:')
        print(margin + 20*'*' + '\n')
        self.outs = 0
        self.bases = [0,0,0]

        print(margin + '%-24s %-20s %-19s %-19s %-19s' % ('Batter', 'Offense', 'Defense', 'Outs', 'Runners'))
        print(margin + '%-24s %-20s %-19s %-19s %-19s' % ('------', '-------','-------', '----', '-------'))
        while self.outs < 3:
            # This random number determines if they get on base or not. 
            a = random.random()
            batter_name = Name.get_player_name(self, self.roster[self.batter][0]) 

            print(margin + '%-25s' % batter_name, end = '')
            # This random number determines how they get on base or how they get out.
            b = random.random()
            if a < lineup[self.batter].ob_pct:
                # Player gets on base.
                if b > 1 - lineup[self.batter].walk_pct:
                    print('%-20s' % 'Walk' , end = '')
                    self.walk()
                elif b <= 1 - lineup[self.batter].walk_pct and b > 1 - lineup[self.batter].ws_pct:
                    print('%-20s' % 'Single', end = '')
                    self.single()
                elif b <= 1 - lineup[self.batter].ws_pct and b > 1 - lineup[self.batter].wsd_pct:
                    print('%-20s' % 'Double', end = '')
                    self.double()
                elif b <= 1-lineup[self.batter].wsd_pct and b > 1-lineup[self.batter].wsdt_pct:
                    print('%-20s' % 'Triple', end = '')
                    self.triple()
                elif b <= 1-lineup[self.batter].wsdt_pct and b > lineup[self.batter].wsdth_pct:
                    print('%-20s' % 'Homerun', end = '')
                    self.homerun()
                elif b <= lineup[self.batter].wsdthh_pct:
                    print('%-20s' % 'Hit by pitch', end = '')
                    self.hit_by_pitch()
                print('%-20s %-20s' % ('', '') , end = '')
            else:
                # player is out
                if b > 1 - lineup[self.batter].str_out_pct:
                    print('%-20s %-20s' % ('', 'Strikeout') , end = '')
                elif b <= 1 - lineup[self.batter].str_out_pct and b > 1 - lineup[self.batter].sogo_pct:
                    print('%-20s %-20s' % ('', 'Ground out') , end = '')
                else:
                    print('%-20s %-20s' % ('', 'Fly out') , end = '')

                self.outs += 1
                print('%-20s' % (self.outs) , end = '')
                
            print('%-20s' % self.bases)

            if self.batter < 8:
                self.batter += 1
            else:
                self.batter = 0
            
            # This is for the slow game to increase suspense between batters!
            if speed.speed == 's':
                time.sleep(2)
        # End of half inning.
        sb.update([[home.team,home.runs, home.hits],[away.team,away.runs, away.hits]])
        # This allows the user to read the plays more closely before moving to the next half inning.
        if speed.speed == 's' or speed.speed == 'm':
            print(input('Press enter key when you are ready to continue.'))
        

class Scoreboard():
        def __intit__(self):
            pass
        
        def update(self,scoreboard_info):
            # scoreboard_info is a list of two lists, the first for home, the second for away.
            # Each list has the team code, team runs, and team hits in that order.
            self.sb = scoreboard_info
            print('\n')
            print(margin + '          SCOREBOARD')
            print(margin + 30*'*')
            print(margin + '{:8}{:8}{:8} {:8}'.format(' ','Team','Runs','Hits'))
            print(margin + '{:8}{:8}{:3d}{:9d}'.format('Home',self.sb[0][0],self.sb[0][1], self.sb[0][2]))
            print(margin + '{:8}{:8}{:3d}{:9d}'.format('Away',self.sb[1][0],self.sb[1][1], self.sb[1][2]))
            print(margin + 30*'*')
            print('\n\n') #, margin, end =  '')

class Final_Results():
    def __init__(self, score, team):
        # The home team is listed first in score and team lists.
        self.score = score
        self.team = team
        print(margin + 75*'*' + '\n')
        print(margin + 'Final Results: \n')
        if score[0] > score[1]:
            print(margin + 'The ' + team[0] + ' defeat the ' + team[1] + ' at home ' + str(score[0]) + ' to ' + str(score[1]) + '.')
        elif score[1] > score[0]:
            print(margin + 'The ' + team[1] + ' defeat the ' + team[0] + ' on the road ' + str(score[1]) + ' to ' + str(score[0]) + '.')
        else:
            print(margin + 'The ' + team[0] + ' tie the ' + team[1] + ' at home ' + str(score[0]) + ' to ' + str(score[1]) + '.')
        print('\n' + margin + 75*'*')



#####################
# Main program
#####################

import random
import time
import sys
global margin
margin = 10*' '
Play = True

while Play == True:
    # Set up the home team 
    ht = Team()
    ht.get_team('home')
    home = Action()
    home.add_players(ht.year,ht.team,ht.name)
    Stats.display(home,home.roster, ht.name,'home')
    # Load stats for each home player
    h1 = Player_Stats(home.roster[0][0])
    h1.add_stats(home.roster[0])
    h2 = Player_Stats(home.roster[1][0])
    h2.add_stats(home.roster[1])
    h3 = Player_Stats(home.roster[2][0])
    h3.add_stats(home.roster[2])
    h4 = Player_Stats(home.roster[3][0])
    h4.add_stats(home.roster[3])
    h5 = Player_Stats(home.roster[4][0])
    h5.add_stats(home.roster[4])
    h6 = Player_Stats(home.roster[5][0])
    h6.add_stats(home.roster[5])
    h7 = Player_Stats(home.roster[6][0])
    h7.add_stats(home.roster[6])
    h8 = Player_Stats(home.roster[7][0])
    h8.add_stats(home.roster[7])
    h9 = Player_Stats(home.roster[8][0])
    h9.add_stats(home.roster[8])


    # Set up the visiting team
    at = Team()
    at.get_team('away')
    away = Action()
    away.add_players(at.year,at.team,at.name)
    Stats.display(away,away.roster,at.name,'away')
    # Load stats for each visiting player
    a1 = Player_Stats(away.roster[0][0])
    a1.add_stats(away.roster[0])
    a2 = Player_Stats(away.roster[1][0])
    a2.add_stats(away.roster[1])
    a3 = Player_Stats(away.roster[2][0])
    a3.add_stats(away.roster[2])
    a4 = Player_Stats(away.roster[3][0])
    a4.add_stats(away.roster[3])
    a5 = Player_Stats(away.roster[4][0])
    a5.add_stats(away.roster[4])
    a6 = Player_Stats(away.roster[5][0])
    a6.add_stats(away.roster[5])
    a7 = Player_Stats(away.roster[6][0])
    a7.add_stats(away.roster[6])
    a8 = Player_Stats(away.roster[7][0])
    a8.add_stats(away.roster[7])
    a9 = Player_Stats(away.roster[8][0])
    a9.add_stats(away.roster[8])

    # Have user set game speed.
    # Note: speed is set as global variable.
    speed = Game_Speed()
    
    # User selects the number of innings to play.
    innings = Game_Innings()

    # Initialize the scoreboard.
    sb = Scoreboard()

    # Loop through each half inning.
    for inning in range(0, int(innings.innings)):
        Game_Engine.play_ball(away,'Top')
        Game_Engine.play_ball(home,'Bottom')

    # Display the final results.
    final = Final_Results([home.runs,away.runs],[ht.name,at.name])

    # Play again?
    print('\n\n')
    play_again = input('Play again? (y or n) ')
    while str(play_again).lower() not in ['y','n']:
            play_again = input('Play again? (y or n) ')
    if play_again == 'n':
        print('\n\n')
        print(margin + 'Thanks for playing!\n\n')
        time.sleep(5)
        sys.exit(0)




