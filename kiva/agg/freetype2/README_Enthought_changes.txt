Notes On Enthought Changes
==========================

The Freetype 2.3.12 source included in this directory is functionally complete.
However, some ancillary files and documentation have been removed in order to
reduce the size of the source checkout for users of the Enthought libraries,
who will not be interfacing directly with Freetype.  The removed files are
listed below.

If you wish to obtain the full, original source of the Freetype library, please
visit one of the following web sites:

        http://freetype.sourceforge.net/
        http://www.freetype.org

Files Removed
=============

ChangeLog
ChangeLog.20
ChangeLog.21
ChangeLog.22
docs/CHANGES

docs/reference/*:
    docs/reference/README
    docs/reference/ft2-base_interface.html
    docs/reference/ft2-basic_types.html
    docs/reference/ft2-bdf_fonts.html
    docs/reference/ft2-bitmap_handling.html
    docs/reference/ft2-cache_subsystem.html
    docs/reference/ft2-cid_fonts.html
    docs/reference/ft2-computations.html
    docs/reference/ft2-font_formats.html
    docs/reference/ft2-gasp_table.html
    docs/reference/ft2-glyph_management.html
    docs/reference/ft2-glyph_stroker.html
    docs/reference/ft2-glyph_variants.html
    docs/reference/ft2-gx_validation.html
    docs/reference/ft2-gzip.html
    docs/reference/ft2-header_file_macros.html
    docs/reference/ft2-incremental.html
    docs/reference/ft2-index.html
    docs/reference/ft2-lcd_filtering.html
    docs/reference/ft2-list_processing.html
    docs/reference/ft2-lzw.html
    docs/reference/ft2-mac_specific.html
    docs/reference/ft2-module_management.html
    docs/reference/ft2-multiple_masters.html
    docs/reference/ft2-ot_validation.html
    docs/reference/ft2-outline_processing.html
    docs/reference/ft2-pfr_fonts.html
    docs/reference/ft2-quick_advance.html
    docs/reference/ft2-raster.html
    docs/reference/ft2-sfnt_names.html
    docs/reference/ft2-sizes_management.html
    docs/reference/ft2-system_interface.html
    docs/reference/ft2-toc.html
    docs/reference/ft2-truetype_engine.html
    docs/reference/ft2-truetype_tables.html
    docs/reference/ft2-type1_tables.html
    docs/reference/ft2-user_allocation.html
    docs/reference/ft2-version.html
    docs/reference/ft2-winfnt_fonts.html

builds/*:
    builds/amiga/include/freetype/config/ftconfig.h
    builds/amiga/include/freetype/config/ftmodule.h
    builds/amiga/makefile
    builds/amiga/makefile.os4
    builds/amiga/README
    builds/amiga/smakefile
    builds/amiga/src/base/ftdebug.c
    builds/amiga/src/base/ftsystem.c
    builds/ansi/ansi-def.mk
    builds/ansi/ansi.mk
    builds/atari/ATARI.H
    builds/atari/deflinejoiner.awk
    builds/atari/FNames.SIC
    builds/atari/FREETYPE.PRJ
    builds/atari/gen-purec-patch.sh
    builds/atari/README.TXT
    builds/beos/beos-def.mk
    builds/beos/beos.mk
    builds/beos/detect.mk
    builds/compiler/ansi-cc.mk
    builds/compiler/bcc-dev.mk
    builds/compiler/bcc.mk
    builds/compiler/emx.mk
    builds/compiler/gcc-dev.mk
    builds/compiler/gcc.mk
    builds/compiler/intelc.mk
    builds/compiler/unix-lcc.mk
    builds/compiler/visualage.mk
    builds/compiler/visualc.mk
    builds/compiler/watcom.mk
    builds/compiler/win-lcc.mk
    builds/detect.mk
    builds/dos/detect.mk
    builds/dos/dos-def.mk
    builds/dos/dos-emx.mk
    builds/dos/dos-gcc.mk
    builds/dos/dos-wat.mk
    builds/exports.mk
    builds/freetype.mk
    builds/link_dos.mk
    builds/link_std.mk
    builds/mac/ascii2mpw.py
    builds/mac/FreeType.m68k_cfm.make.txt
    builds/mac/FreeType.m68k_far.make.txt
    builds/mac/FreeType.ppc_carbon.make.txt
    builds/mac/FreeType.ppc_classic.make.txt
    builds/mac/ftlib.prj.xml
    builds/mac/ftmac.c
    builds/mac/README
    builds/modules.mk
    builds/newline
    builds/os2/detect.mk
    builds/os2/os2-def.mk
    builds/os2/os2-dev.mk
    builds/os2/os2-gcc.mk
    builds/symbian/bld.inf
    builds/symbian/freetype.mmp
    builds/toplevel.mk
    builds/unix/.gitignore
    builds/unix/aclocal.m4
    builds/unix/config.guess
    builds/unix/config.log
    builds/unix/config.status
    builds/unix/config.sub
    builds/unix/configure
    builds/unix/configure.ac
    builds/unix/configure.raw
    builds/unix/detect.mk
    builds/unix/freetype-config
    builds/unix/freetype-config.in
    builds/unix/freetype2.in
    builds/unix/freetype2.m4
    builds/unix/freetype2.pc
    builds/unix/ft-munmap.m4
    builds/unix/ft2unix.h
    builds/unix/ftconfig.h
    builds/unix/ftconfig.in
    builds/unix/ftsystem.c
    builds/unix/install-sh
    builds/unix/install.mk
    builds/unix/libtool
    builds/unix/ltmain.sh
    builds/unix/mkinstalldirs
    builds/unix/unix-cc.in
    builds/unix/unix-cc.mk
    builds/unix/unix-def.in
    builds/unix/unix-def.mk
    builds/unix/unix-dev.mk
    builds/unix/unix-lcc.mk
    builds/unix/unix.mk
    builds/unix/unixddef.mk
    builds/vms/ftconfig.h
    builds/vms/ftsystem.c
    builds/win32/detect.mk
    builds/win32/ftdebug.c
    builds/win32/vc2005/freetype.sln
    builds/win32/vc2005/freetype.vcproj
    builds/win32/vc2005/index.html
    builds/win32/vc2008/freetype.sln
    builds/win32/vc2008/freetype.vcproj
    builds/win32/vc2008/index.html
    builds/win32/visualc/freetype.dsp
    builds/win32/visualc/freetype.dsw
    builds/win32/visualc/freetype.sln
    builds/win32/visualc/freetype.vcproj
    builds/win32/visualc/index.html
    builds/win32/visualce/freetype.dsp
    builds/win32/visualce/freetype.dsw
    builds/win32/visualce/freetype.vcproj
    builds/win32/visualce/index.html
    builds/win32/w32-bcc.mk
    builds/win32/w32-bccd.mk
    builds/win32/w32-dev.mk
    builds/win32/w32-gcc.mk
    builds/win32/w32-icc.mk
    builds/win32/w32-intl.mk
    builds/win32/w32-lcc.mk
    builds/win32/w32-mingw32.mk
    builds/win32/w32-vcc.mk
    builds/win32/w32-wat.mk
    builds/win32/win32-def.mk
    builds/wince/ftdebug.c
    builds/wince/vc2005-ce
    builds/wince/vc2005-ce/freetype.sln
    builds/wince/vc2005-ce/freetype.vcproj
    builds/wince/vc2005-ce/index.html
    builds/wince/vc2008-ce
    builds/wince/vc2008-ce/freetype.sln
    builds/wince/vc2008-ce/freetype.vcproj
    builds/wince/vc2008-ce/index.html

