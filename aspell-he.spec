%define _enable_debug_packages %{nil}
%define debug_package          %{nil}

%define src_ver 1.0-0
%define fname aspell6-%{languagecode}
%define aspell_ver 0.60
%define languageenglazy Hebrew
%define languagecode he
%define lc_ctype he_IL

Summary:	%{languageenglazy} files for aspell
Name:		aspell-%{languagecode}
Version:	1.0.0
Release:	17
Group:		System/Internationalization
License:	GPLv2
Url:		http://aspell.net/
Source0:	http://ftp.gnu.org/gnu/aspell/dict/%{languagecode}/%{fname}-%{src_ver}.tar.bz2

BuildRequires:	aspell >= %{aspell_ver}
Requires:	aspell >= %{aspell_ver}
# Mandriva Stuff
Requires:	locales-%{languagecode}
# aspell = 1, myspell = 2, lang-specific = 3
Provides:	enchant-dictionary = 1
Provides:	aspell-dictionary
Provides:	aspell-%{lc_ctype}
Provides:	spell-%{languagecode}
Autoreqprov:	no

%description
A %{languageenglazy} dictionary for use with aspell, a spelling checker.

%prep
%setup -qn %{fname}-%{src_ver}
iconv -f ISO-8859-15 -t utf-8 README.iso -o README.iso.aux
mv -f README.iso.aux README.iso

%build
# don't use configure macro
./configure

%make

%install
%makeinstall_std

chmod 644 Copyright README* 

%files
%doc README* Copyright
%{_libdir}/aspell-%{aspell_ver}/*

