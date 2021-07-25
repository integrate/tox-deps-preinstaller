import pluggy, os

hookimpl = pluggy.HookimplMarker("tox")

# @hookimpl
# def tox_configure(config):
#     print(config)

@hookimpl
def tox_testenv_install_deps(venv, action):
    if action.name==".package":
        return

    venv.envconfig.usedevelop=True

    path = "C:/Users/vmatv/PycharmProjects/pygame_wrap1"
    venv.envconfig.commands.insert(0, ["pip", "install", "-e", path])
    print("commands:", venv.envconfig.commands)
