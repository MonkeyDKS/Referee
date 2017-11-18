"""
Constants for usage throughout the entire bot
If you plan to self host this bot, edit them to contain values from your server
"""
import re
from collections import OrderedDict
from disco.types.guild import GuildMember
from holster.enum import Enum

###Constants
CONTROL_CHANNEL = 375605052171354122
PLAYING_STATUS = 'Managing all the things'
GLOBAL_ADMINS = [188918216008007680, 134146475591467008]
MOD_ROLE = 370594147511566336
DEV_ROLE = 294473442164604929
PY_CODE_BLOCK = u'```py\n{}\n```'
TEAM_CATEGORY = 355983461825380352
REACTIONS_MESSAGE = 381068629627764736
EMOJIS = {377098801095114753: 'MMTestGame',
          377098801195909122: 'MMOW',
          377098801384652800: 'MMUHC',
          377098801397235722: 'MMRL',
          377098801573527564: 'MMPUBG',
          377099565033062400: 'MMMC',
          377100326655885312: 'MMEvening_UHC',
          377100326731251712: 'MMMorning_UHC',
          379104082079514637: 'MMTeamAqua',
          379104082461458432: 'MMTeamGreen',
          379104087679041538: 'MMTeamGold',
          379104088098471956: 'MMTeamYellow',
          379104088102535169: 'MMTeamRed',
          379104088111185920: 'MMTeamPurple',
          379104088111185922: 'MMTeamPink',
          379104088232558592: 'MMTeamOrange',
          379104088257724416: 'MMTeamBlue',
          379104088442535946: 'MMTeamDarkRed'
         }
GAME_INFO_STEPS = OrderedDict([
    ('get_name', 'Okay, please give the name of the new game'),
    ('get_desc', 'Okay, created the game. now, give a description for the game'),
    ('should_create_channels', 'Should I create channels for this game?')
])
GAME_ADD_STEPS = {
    'validate': 'This will start the proces of {}. Is this correct?'.format(
        'creating a new game',
    ),
    'complete': 'Created game `{}`, with description `{}`. I `will{}` create channels for it.',
    'fail': 'Process canceled. Restart it by using `!game add`'
}
MC_UUID_URL = 'https://api.mojang.com/users/profiles/minecraft/{}'

###Enums

CommandLevel = Enum(
    MOD=2,
    DEV=1
)

###Functions
def check_global_admin(uid):
    """Checks if user is global admin and thus can use all commands"""
    return bool(uid in GLOBAL_ADMINS)

def get_user_level(user):
    """Gets user level for certain user"""
    user = user # type: GuildMember
    if MOD_ROLE in user.roles:
        return 2
    elif DEV_ROLE in user.roles:
        return 1
    else:
        return 0

###Regexes
BATTLE_TAG = re.compile(r'^[a-z][a-z0-9]{2,11}#[0-9]{4,5}', re.I)
MC_NAME = re.compile(r'[a-z0-9_]{1,16}', re.I)
MC_UUID = re.compile(r'[0-9a-f]{32}')
STEAM_NAME = re.compile(r'[a-z0-9_]{3,}', re.I)
