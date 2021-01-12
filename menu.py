from main_online import main_online
from consolemenu import SelectionMenu, MenuFormatBuilder
from consolemenu.format import MenuBorderStyleType
import main_offline
import main_online
from colors.colors import *
from persist_data import *


menu_format = MenuFormatBuilder().set_border_style_type(MenuBorderStyleType.HEAVY_BORDER) \
    .set_prompt(">> ") \
    .set_title_align('center') \
    .set_subtitle_align('center') \
    .set_left_margin(4) \
    .set_right_margin(4) \
    .show_header_bottom_border(True)

select = ["Mode Local", "Mode en Ligne", "Options", "Quitter"]
link = [main_offline.main_loop, main_online.main_online,
        main_online.main_online, exit]
menu = SelectionMenu(select, f"LeLonMo v{version}", subtitle="Le jeu du long mot",
                prologue_text="Choisisser votre mode de jeu :", show_exit_option=False, formatter=menu_format)
menu.show()
menu.join()
link[menu.selected_option]()
