---
title: Setup
layout: default
---

This is a guide to setting up a Linux box with my perferred software and config settings.

I have a personal package repository that includes a meta package for
installing all my preferred software as well as personal builds of dwm and
simple terminal.

On Arch add the repository to the pacman config:

    cat <<EOT >> /etc/pacman.conf
    [hedaleth]
    SigLevel = Optional TrustAll
    Server = https://arch.hedaleth.net/
    EOT

On Debian or Ubuntu add the repository to the sources list where {version} can be buster, bionic or disco:

    echo deb [arch=amd64 trusted=yes] http://debian.hedaleth.net.s3-website.eu-west-2.amazonaws.com {version} main >> /etc/sources.list

In home directory clone config files from git repo:

    git init

    git remote add origin git@github.com:edclements/dotfiles.git

    git pull

    git submodule update --init

