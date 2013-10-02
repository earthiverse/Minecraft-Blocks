#!/usr/bin/env python3
import os, subprocess, sys, tempfile, zipfile

in_zip = zipfile.ZipFile(sys.argv[1], 'r')
out_zip = zipfile.ZipFile("out.zip", 'w', zipfile.ZIP_DEFLATED)
all_files = set(in_zip.namelist())
bad_files = set()

# Remove un-needed stuff from zip
for f in all_files:
	print(f)
	## The Files That Matter
	if "assets/minecraft/textures/blocks" not in f	and "assets/minecraft/textures/items" not in f:
		bad_files.add(f)

	## Other Useless Files
	if "Thumbs.db" in f:
		bad_files.add(f)
	elif f.endswith(".mcmeta"):
		bad_files.add(f)
	## We only care about pngs
	elif ".png" not in f:
		bad_files.add(f)

# Put everything that's left in a 'good' zip file
for f in set.difference(all_files, bad_files):
	print("\n\n")
	print(f)
	# Read from Zip
	temp_in = in_zip.read(f)

	## Optimize
	# Make Temp File
	temp_img = tempfile.NamedTemporaryFile(delete=False)
	temp_img.write(temp_in)
	temp_img.close()

	# Optimize
	subprocess.call(["optipng", "-o5", "-strip all", "-out", temp_img.name, temp_img.name])

	# Write to Zip
	temp_img = open(temp_img.name, 'rb')
	out_zip.writestr(f, temp_img.read())
	temp_img.close()

	# Remove Temporary File
	os.unlink(temp_img.name)
