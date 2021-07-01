import matplotlib.colors
import seaborn as sns

# Color palette
blue_rgb       = (78/255,  121/255, 167/255)
orange_rgb     = (242/255, 142/255, 43/255)
red_rgb        = (225/255, 87/255,  89/255)
turquoise_rgb  = (118/255, 183/255, 178/255)
green_rgb      = (89/255,  161/255, 79/255)
yellow_rgb     = (237/255, 201/255, 72/255)
purple_rgb     = (176/255, 122/255, 161/255)
pink_rgb       = (255/255, 157/255, 167/255)
brown_rgb      = (156/255, 117/255, 95/255)
gray_rgb       = (186/255, 176/255, 172/255)

sns_saturation = 1

palette_def = [blue_rgb,
               orange_rgb,
               red_rgb,
               turquoise_rgb,
               green_rgb,
               yellow_rgb,
               purple_rgb,
               pink_rgb,
               brown_rgb,
               gray_rgb]

# Blues (2 shades)
blue_shades = [(78/255,  121/255, 167/255),
               (163/255, 201/255, 220/255)]

# More color definitions
conf_cmap = matplotlib.colors.LinearSegmentedColormap.from_list("", [(255/255,255/255,215/255), turquoise_rgb, blue_rgb])
pos_cmap =  matplotlib.colors.LinearSegmentedColormap.from_list("", [(205/255,242/255,246/255),(23/255,39/255,82/255)])
neg_pos_cmap =  matplotlib.colors.LinearSegmentedColormap.from_list("", [blue_rgb,orange_rgb])

# Style definitions
sns.set_style({'axes.facecolor': 'white',
               'axes.edgecolor': '.8',
               'axes.grid': True,
               'axes.axisbelow': True,
               'axes.labelcolor': '.15',
               'figure.facecolor': 'white',
               'grid.color': '.8',
               'grid.linestyle': '-',
               'text.color': '.15',
               'xtick.color': '.15',
               'ytick.color': '.15',
               'xtick.direction': 'out',
               'ytick.direction': 'out',
               'lines.solid_capstyle': 'round',
               'patch.edgecolor': 'w',
               'image.cmap': 'rocket',
               'font.family': ['sans-serif'],
               'font.sans-serif': ['Arial',
               'DejaVu Sans',
               'Liberation Sans',
               'Bitstream Vera Sans',
               'sans-serif'],
               'patch.force_edgecolor': False,
               'xtick.bottom': False,
               'xtick.top': False,
               'ytick.left': False,
               'ytick.right': False,
               'axes.spines.left': False,
               'axes.spines.bottom': True,
               'axes.spines.right': False,
               'axes.spines.top': False}
)
matplotlib.rcParams.update({'font.size': 15})


# Seed
seed = 27

# Number of folder CV
n_folds = 5

# Mapping emotions
emotion_id_to_emotion = {'adm':'admiration',
                         'amu':'amusement',
                         'att':'tenderness',
                         'col':'anger',
                         'deg':'disgust',
                         'des':'despair',
                         'fie':'pride',
                         'hon':'shame',
                         'inq':'anxiety',
                         'int':'interest',
                         'irr':'irritation',
                         'joi':'joy',
                         'mep':'contempt',
                         'peu':'panic',
                         'pla':'pleasure',
                         'sou':'relief',
                         'sur':'surprise',
                         'tri':'sadness'
                        }
emotion_to_emotion_id = dict(zip(emotion_id_to_emotion.values(), emotion_id_to_emotion.keys()))

emotion_fr_id_to_emotion_eng_id = {'adm':'adm',
                                   'amu':'amu',
                                   'att':'ten',
                                   'col':'ang',
                                   'deg':'dis',
                                   'des':'des',
                                   'fie':'pri',
                                   'hon':'sha',
                                   'inq':'anx',
                                   'int':'int',
                                   'irr':'irr',
                                   'joi':'joy',
                                   'mep':'con',
                                   'peu':'fea',
                                   'pla':'ple',
                                   'sou':'rel',
                                   'sur':'sur',
                                   'tri':'sad'
                                  }
emotion_eng_id_to_emotion_fr_id = dict(zip(emotion_fr_id_to_emotion_eng_id.values(), emotion_fr_id_to_emotion_eng_id.keys()))

emotion_id_to_emotion_num = {'adm':0,
                             'amu':1,
                             'att':2,
                             'col':3,
                             'deg':4,
                             'des':5,
                             'fie':6,
                             'hon':7,
                             'inq':8,
                             'int':9,
                             'irr':10,
                             'joi':11,
                             'mep':12,
                             'peu':13,
                             'pla':14,
                             'sou':15,
                             'sur':16,
                             'tri':17
                            }
emotion_num_to_emotion_id = dict(zip(emotion_id_to_emotion_num.values(), emotion_id_to_emotion_num.keys()))

emotion_eng_id_to_emotion_num = {'adm':0,
                                 'amu':1,
                                 'ten':2,
                                 'ang':3,
                                 'dis':4,
                                 'des':5,
                                 'pri':6,
                                 'sha':7,
                                 'anx':8,
                                 'int':9,
                                 'irr':10,
                                 'joy':11,
                                 'con':12,
                                 'fea':13,
                                 'ple':14,
                                 'rel':15,
                                 'sur':16,
                                 'sad':17
                                }
emotion_num_to_emotion_eng_id = dict(zip(emotion_eng_id_to_emotion_num.values(), emotion_eng_id_to_emotion_num.keys()))


emotion_id_to_valence = {'adm':'pos',
                         'amu':'pos',
                         'att':'pos',
                         'col':'neg',
                         'deg':'neg',
                         'des':'neg',
                         'fie':'pos',
                         'hon':'neg',
                         'inq':'neg',
                         'int':'pos',
                         'irr':'neg',
                         'joi':'pos',
                         'mep':'neg',
                         'peu':'neg',
                         'pla':'pos',
                         'sou':'pos',
                         'sur':'pos',
                         'tri':'neg'
                         }


# Mapping actor_id to sex
actor_id_to_sex = {1:'m',
                   2:'f',
                   3:'m',
                   4:'m',
                   5:'m',
                   6:'f',
                   7:'f',
                   8:'m',
                   9:'f',
                   10:'f',
                   }
