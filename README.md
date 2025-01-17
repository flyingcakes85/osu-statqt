<!-- Logo -->

<p align="center">
  <img width="500px" src="Assets/Logo/logo1x.png">
</p>

# Osu!StatQt

Osu statistics right on your desktop, made with Qt5

A lightweight desktop application to show you information about plays, scores and beatmaps. Basically a simplified osu-web client.

## Status

Currently, it is a passion project for me and I'm creating this to learn the pyQt framework and more stuff about Python. I plan on adding features to it with time and frequent releases as well until its fully complete or there are changes in osu API V2.

In its alpha stage, this is just the barebones with basic features. With the subsequent beta and stable releases, the featureset would only increase.

## Installing Osu!StatQt

Binaries are only available for windows as of now, but you can always run the python script from the source files on any operating system with python and its dependencies installed.

**Latest Release:**

| [Windows 8.1+ (x64)](https://github.com/sortedcord/osu-statqt/releases) | 
| ------------- |

## Configuring Osu!StatQt

OsuStat uses Circleguard's [ossapiV2](https://github.com/circleguard/ossapi) which is a python wrapper for Osu-api V2. This requires you to create a OAuth Application in your [osu account settings](https://osu.ppy.sh/home/account/edit)

![apitutorial](https://user-images.githubusercontent.com/37407370/147528626-cb381857-5d54-464d-9bb7-e9ca6602927b.gif)

<i>Note: I may have shown my client-secret and client-id but that is only for demonstrational purposes and are dummy values. Do not share these credentials with anyone else as very risky and may have your account compromised.</i>

For the Callback Url you can have any localhost port which is not in use.

## Building Osu!StatQt

I use `pyinstaller` for building and managing packages for OsuStatQt. It is highly recommended to use a virtual environment when building with pyinstaller.

[Circleguard's ossapi](https://github.com/circleguard/ossapi) causes issues with pyinstaller as for some reason its not able to read the dumped token files. Instead I suggest using https://github.com/sortedcord/ossapi which I have modified to not dump the tokens at all.

``` bash
# Assuming this is in a venv

git clone https://github.com/sortedcord/ossapi
cd ossapi
pip install -e .
```

Other dependencies which you will need include `PyQt5` and `PyQt5-tools`

``` bash
pip install PyQt5 PyQt5-tools
```

``` bash
# In a separate folder

git clone https://github.com/sortedcord/osu-statqt.git
cd osu-statqt
```
### Windows 8.1+ and GNU/Linux


#### Default Build
```powershell
pyinstaller --noconsole --add-data="Assets/Logo/icon48x.ico;."  .\osuStatQt.py --noconfirm --name="OsuStatQt" --icon="Assets/Logo/icon256x.ico"
```

#### Debug Build

Just remove the `--noconcole` flag to see the console when the app is run.

```powershell
pyinstaller --add-data="Assets/Logo/icon48x.ico;."  .\osuStatQt.py --noconfirm --name="OsuStatQt" --icon="Assets/Logo/icon256x.ico"
```

#### Standalone Build

Use the `--onefile` flag to compile this into a single file

```powershell
pyinstaller --onefile --add-data="Assets/Logo/icon48x.ico;."  .\osuStatQt.py --noconfirm --name="OsuStatQt" --icon="Assets/Logo/icon256x.ico"
```

### Mac OS (Catalina and above)

I don't own a Mac nor am I interested in setting up a hackintosh, so practically there is no way for me to test the mac os build, however the process of building binaries is more or less the same, the only catch is to build a standalone binary.

```bash
pyinstaller --onefile --add-data="Assets/Logo/icon48x.ico;."  .\osuStatQt.py --noconfirm --name="OsuStatQt" --icon="Assets/Logo/icon256x.ico"
```



## Credits

Would like to thank these creators for their projects and contributions.

- [ppy, osu-web API & osu-resources](https://github.com/peppy)
- [circleguard: osuAPI, licensed under GPL-3.0 License](https://github.com/circleguard/ossapi)
