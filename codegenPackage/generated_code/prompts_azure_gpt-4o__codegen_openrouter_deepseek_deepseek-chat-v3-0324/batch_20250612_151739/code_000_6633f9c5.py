"""
Generated Code Metadata:
========================
Original URL: https://flashcoin.trade
Prompt: Write code to configure a LiteSpeed Web Server for hosting a directory listing similar to the one shown at flashcoin.trade.
Generated: DETERMINISTIC_6633f9c52d61c2ff
Batch ID: 20250612_151739
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```apache
# LiteSpeed Web Server Configuration for Directory Listing
# Place this in your virtual host configuration or .htaccess file

<IfModule LiteSpeed>
    # Enable directory listing
    Options +Indexes

    # Customize the directory listing appearance
    IndexOptions FancyIndexing HTMLTable NameWidth=* DescriptionWidth=* 
    IndexOptions IconHeight=16 IconWidth=16 SuppressHTMLPreamble
    IndexOptions IgnoreCase FoldersFirst VersionSort XHTML

    # Set header and footer files
    HeaderName /header.html
    ReadmeName /footer.html

    # Custom icons for different file types
    AddIconByEncoding (CMP,/icons/compressed.gif) x-compress x-gzip
    AddIconByType (TXT,/icons/text.gif) text/*
    AddIconByType (IMG,/icons/image2.gif) image/*
    AddIconByType (SND,/icons/sound2.gif) audio/*
    AddIconByType (VID,/icons/movie.gif) video/*
    AddIcon /icons/binary.gif .bin .exe
    AddIcon /icons/binhex.gif .hqx
    AddIcon /icons/tar.gif .tar
    AddIcon /icons/world2.gif .wrl .wrl.gz .vrml .vrm .iv
    AddIcon /icons/compressed.gif .Z .z .tgz .gz .zip
    AddIcon /icons/a.gif .ps .ai .eps
    AddIcon /icons/layout.gif .html .shtml .htm .pdf
    AddIcon /icons/text.gif .txt
    AddIcon /icons/c.gif .c
    AddIcon /icons/p.gif .pl .py
    AddIcon /icons/f.gif .for
    AddIcon /icons/dvi.gif .dvi
    AddIcon /icons/uuencoded.gif .uu
    AddIcon /icons/script.gif .conf .sh .shar .csh .ksh .tcl
    AddIcon /icons/tex.gif .tex
    AddIcon /icons/bomb.gif core
    AddIcon /icons/back.gif ..
    AddIcon /icons/hand.right.gif README
    AddIcon /icons/folder.gif ^^DIRECTORY^^
    AddIcon /icons/blank.gif ^^BLANKICON^^

    # Default icon for unknown file types
    DefaultIcon /icons/unknown.gif

    # Add description for certain file types
    AddDescription "GZIP compressed TAR archive" .tgz
    AddDescription "GZIP compressed archive" .Z .gz
    AddDescription "TAR compressed archive" .tar
    AddDescription "ZIP compressed archive" .zip
    AddDescription "RAR compressed archive" .rar
    AddDescription "StuffIt compressed archive" .sit
    AddDescription "Macintosh BinHex archive" .hqx
    AddDescription "UUEncoded file" .uu
    AddDescription "HTML document" .html .htm
    AddDescription "Plain text file" .txt
    AddDescription "Perl script" .pl
    AddDescription "Python script" .py
    AddDescription "Shell script" .sh
    AddDescription "JPEG image" .jpg .jpeg
    AddDescription "GIF image" .gif
    AddDescription "PNG image" .png
    AddDescription "MP3 audio" .mp3
    AddDescription "MPEG video" .mpeg .mpg
    AddDescription "PDF document" .pdf
    AddDescription "Microsoft Word document" .doc
    AddDescription "Microsoft Excel document" .xls
    AddDescription "Microsoft PowerPoint document" .ppt

    # Set default sorting by name
    IndexOrderDefault Ascending Name

    # Allow HTML in directory listings
    IndexIgnore .??* *~ *# HEADER* README* RCS CVS *,v *,t

    # Custom error documents
    ErrorDocument 400 /error/400.html
    ErrorDocument 401 /error/401.html
    ErrorDocument 403 /error/403.html
    ErrorDocument 404 /error/404.html
    ErrorDocument 500 /error/500.html
</IfModule>
```
