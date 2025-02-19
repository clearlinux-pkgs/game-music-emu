#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: cmake
# autospec version: v21
# autospec commit: e36a856
#
Name     : game-music-emu
Version  : 0.6.4
Release  : 3
URL      : https://github.com/libgme/game-music-emu/archive/0.6.4/game-music-emu-0.6.4.tar.gz
Source0  : https://github.com/libgme/game-music-emu/archive/0.6.4/game-music-emu-0.6.4.tar.gz
Summary  : A video game emulation library for music.
Group    : Development/Tools
License  : GPL-2.0
Requires: game-music-emu-bin = %{version}-%{release}
Requires: game-music-emu-lib = %{version}-%{release}
Requires: game-music-emu-license = %{version}-%{release}
BuildRequires : buildreq-cmake
BuildRequires : pkgconfig(sdl2)
BuildRequires : zlib-dev
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
Game_Music_Emu 0.6.4: Game Music Emulators
------------------------------------------
Game_Music_Emu is a collection of video game music file emulators that
support the following formats and systems:

%package bin
Summary: bin components for the game-music-emu package.
Group: Binaries
Requires: game-music-emu-license = %{version}-%{release}

%description bin
bin components for the game-music-emu package.


%package dev
Summary: dev components for the game-music-emu package.
Group: Development
Requires: game-music-emu-lib = %{version}-%{release}
Requires: game-music-emu-bin = %{version}-%{release}
Provides: game-music-emu-devel = %{version}-%{release}
Requires: game-music-emu = %{version}-%{release}

%description dev
dev components for the game-music-emu package.


%package lib
Summary: lib components for the game-music-emu package.
Group: Libraries
Requires: game-music-emu-license = %{version}-%{release}

%description lib
lib components for the game-music-emu package.


%package license
Summary: license components for the game-music-emu package.
Group: Default

%description license
license components for the game-music-emu package.


%prep
%setup -q -n game-music-emu-0.6.4
cd %{_builddir}/game-music-emu-0.6.4
## copy_prepend content
echo -e "\ninstall(TARGETS gme_player RUNTIME DESTINATION %{_bindir})" >> player/CMakeLists.txt
## copy_prepend end

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1739812228
mkdir -p clr-build
pushd clr-build
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export GOAMD64=v2
%cmake ..   -G 'Unix Makefiles'
make  %{?_smp_mflags}  all \
gme_player
popd

%install
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export SOURCE_DATE_EPOCH=1739812228
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/game-music-emu
cp %{_builddir}/game-music-emu-%{version}/license.gpl2.txt %{buildroot}/usr/share/package-licenses/game-music-emu/4cc77b90af91e615a64ae04893fdffa7939db84c || :
export GOAMD64=v2
GOAMD64=v2
pushd clr-build
%make_install
popd
## install_append content
make -C clr-build/player install DESTDIR=%{buildroot}
## install_append end

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/gme_player

%files dev
%defattr(-,root,root,-)
/usr/include/gme/gme.h
/usr/lib64/libgme.so
/usr/lib64/pkgconfig/libgme.pc

%files lib
%defattr(-,root,root,-)
/usr/lib64/libgme.so.0
/usr/lib64/libgme.so.0.6.4

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/game-music-emu/4cc77b90af91e615a64ae04893fdffa7939db84c
