---
title: Command Reference
layout: default
---

terminal
--------

**CTRL+T** - Fuzzy search for files

**CTRL+Z** - Stop foreground program

`fg` - Restore stopped program to foreground

`bg job_id` - Resume stopped program in background

`jobs` - Show running and stopped programs

tmux
----

<table>
<tr><th style="width:250px"></th><th></th></tr>
<tr><td><b>SHIFT+LEFT MOUSE BUTTON</b></td><td> </td><td>Copy to primary clipboard</td></tr>
<tr><td><b>CTRL+B, \</b></td><td> </td><td>Split window with new pane in current path on right</td></tr>
<tr><td><b>CTRL+B, -</b></td><td> </td><td>Split window with new pane in current path at bottom</td></tr>
<tr><td><b>CTRL+B, /</b></td><td> </td><td>New window in current path</td></tr>
</table>

dwm
---

**SUPER+SHIFT+ENTER** - Open terminal window

**SUPER+SHIFT+C** - Close window

**SUPER+P** - Launch dmenu

**SUPER+SHIFT+Q** - Quit DWM

**SUPER+L** - Lock screen

vim
---

**:set list** - Show whitespace

**:syntax sync fromstart** - Fix syntax highlighting

`g-` - Go to older text state

`g+` - Go to newer text state

**CTRL+R,0** - Put last yanked string into command line

files
-----

Extract gzipped tarball

    tar xzvf target.tar.gz

Extract bzipped tarball

    tar xjvf target.tar.bz2

http
----

Fetch JSON and pretty print

    curl URL -s | json_reformat

audio
-----

Start JACK

    jack_control start

Stop JACK

    jack_control stop

systemd
-------

Boot into text mode

    systemctl enable multi-user.target
    sudo systemctl set-default multi-user.target

