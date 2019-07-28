---
title: Command Reference
layout: default
---

terminal
--------

<table class="key-binding">
  <tr><th></th><th></th></tr>
  <tr><td>CTRL+T</td><td>Fuzzy search for files</td></tr>
  <tr><td>CTRL+Z</td><td>Stop foreground program</td></tr>
  <tr><td>fg</td><td>Restore stopped program to foreground</td></tr>
  <tr><td>bg job_id</td><td>Resume stopped program in background</td></tr>
  <tr><td>jobs</td><td>Show running and stopped programs</td></tr>
</table>

tmux
----

<table class="key-binding">
  <tr><th></th><th></th></tr>
  <tr><td>SHIFT+LEFT MOUSE BUTTON</td><td>Copy to primary clipboard</td></tr>
  <tr><td>CTRL+B, \</td><td>Split window with new pane in current path on right</td></tr>
  <tr><td>CTRL+B, -</td><td>Split window with new pane in current path at bottom</td></tr>
  <tr><td>CTRL+B, /</td><td>New window in current path</td></tr>
</table>

dwm
---

<table class="key-binding">
  <tr><th></th><th></th></tr>
  <tr><td>SUPER+SHIFT+ENTER</td><td>Open terminal window</td></tr>
  <tr><td>SUPER+SHIFT+C</td><td>Close window</td></tr>
  <tr><td>SUPER+P</td><td>Launch dmenu</td></tr>
  <tr><td>SUPER+SHIFT+Q</td><td>Quit DWM</td></tr>
  <tr><td>SUPER+L</td><td>Lock screen</td></tr>
</table>

vim
---

<table class="key-binding">
  <tr><th></th><th></th></tr>
  <tr><td>:set list</td><td>Show whitespace</td></tr>
  <tr><td>:syntax sync fromstart</td><td>Fix syntax highlighting</td></tr>
  <tr><td>g-</td><td>Go to older text state</td></tr>
  <tr><td>g+</td><td>Go to newer text state</td></tr>
  <tr><td>CTRL+R, 0</td><td>Put last yanked string into command line</td></tr>
  <tr><td>:g!/pattern/d</td><td>Delete lines not matching pattern</td></tr>
</table>

cmus
----

<table class="key-binding">
  <tr><th></th><th></th></tr>
  <tr><td>y</td><td>Add to playlist</td></tr>
  <tr><td>x</td><td>Play</td></tr>
  <tr><td>c</td><td>Pause</td></tr>
</table>

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

git
---

List branches ordered by last change

    git branch --sort=-committerdate

