#!/usr/bin/env python3
import sys, zipfile

in_zip = zipfile.ZipFile(sys.argv[1], 'r')
out_zip = zipfile.ZipFile("out.zip", 'w', zipfile.ZIP_DEFLATED)
all_files = set(in_zip.namelist())
bad_files = set()

# Remove un-needed stuff from zip
for f in all_files:
    if "Thumbs.db" in f:
        bad_files.add(f)
    elif f.endswith(".mcmeta"):
        bad_files.add(f)
    elif "mcpatcher" in f:
        bad_files.add(f)
    elif "font" in f:
        bad_files.add(f)
    elif "icons" in f:
        bad_files.add(f)
    elif "lang" in f:
        bad_files.add(f)
    elif "Plethora" in f:
        bad_files.add(f)
    elif "texts" in f:
        bad_files.add(f)
        
    elif "textures/aether" in f:
        bad_files.add(f)
    elif "textures/environment" in f:
        bad_files.add(f)
    # textures/font taken care of by previous 'font' in
    elif "textures/gui" in f:
        bad_files.add(f)
    elif "textures/map" in f:
        bad_files.add(f)
    elif "textures/misc" in f:
        bad_files.add(f)
    elif "textures/particle" in f:
        bad_files.add(f)

# Put everything that's left in a 'good' zip file
for f in set.difference(all_files, bad_files):
    temp = in_zip.read(f)
    out_zip.writestr(f, temp)
