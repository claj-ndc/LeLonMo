import os
import platform
import argparse

os_name = platform.system()


parser = argparse.ArgumentParser(description='Play LeLonMo')
parser.add_argument("--server", help="Start the server", action="store_true")
args = parser.parse_args()

if args.server:
    print("[I] Starting server...", end="\r")
    import server.socket_server as server

    # Settings #
    LANGUAGE = "fr"
    PORT = 11111

    main_thread = server.MainThread(PORT)
    main_thread.start()
    while True:
        try:
            u = input()
        except:
            u = "exit"
        if u == "exit":
            try:
                main_thread.tcpsock.close()
            except OSError:
                pass
        exit()
else:
    print("Starting the game, please wait ...")
    print("Checking dependancies ... ")
    try:
        import six
    except:
        print("six is not installed, trying to install it automatically ...")
        import subprocess
        import sys
        command = [sys.executable, "-m", "pip", "install", "six", "--user"]
        subprocess.run(command)
    import lelonmo.persist_data as persist
    if os_name == "Windows" and persist.DATA["game"]['FIRST_RUN']:
        persist.update_key("async_input", True, "online")
        if platform.version().startswith("10."):
            persist.update_key("FIRST_RUN", False, "game")
        elif persist.DATA["game"]['FIRST_RUN']:
            persist.update_key("FIRST_RUN", False, "game")
            input(
                "Colors are not supported on this version of windows, and are disabled by default. ")
            persist.update_key("USE_COLORS", False, "settings")
    elif os_name == "Darwin":
        try:
            import Quartz
            import objc
        except:
            print("Quartz and objc are not installed, trying to install it automatically ...")
            import subprocess
            import sys
            command = [sys.executable, "-m", "pip", "install",
                       "pyobjc-framework-Quartz", "pyobjc", "--user"]
            subprocess.run(command)
    import lelonmo.menu as menu
    menu.main()
