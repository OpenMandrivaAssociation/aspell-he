%define _enable_debug_packages %{nil}
%define debug_package          %{nil}

%define src_ver 1.0-0
%define fname aspell6-%{languagecode}
%define aspell_ver 0.60
%define languageenglazy Hebrew
%define languagecode he
%define lc_ctype he_IL

Summary:       %{languageenglazy} files for aspell
Name:          aspell-%{languagecode}
Version:       1.0.0
Release:       %mkrel 12
Group:         System/Internationalization
Source:        http://ftp.gnu.org/gnu/aspell/dict/%{languagecode}/%{fname}-%{src_ver}.tar.bz2
URL:		   http://aspell.net/
License:	   GPLv2
BuildRoot:     %{_tmppath}/%{name}-%{version}-root
Provides: spell-%{languagecode}

BuildRequires: aspell >= %{aspell_ver}
BuildRequires: make
Requires:      aspell >= %{aspell_ver}

# Mandriva Stuff
Requires:      locales-%{languagecode}
# aspell = 1, myspell = 2, lang-specific = 3
Provides:      enchant-dictionary = 1
Provides:      aspell-dictionary
Provides:      aspell-%{lc_ctype}

Autoreqprov:   no

%description
A %{languageenglazy} dictionary for use with aspell, a spelling checker.

%prep
%setup -q -n %{fname}-%{src_ver}
iconv -f ISO-8859-15 -t utf-8 README.iso -o README.iso.aux
mv -f README.iso.aux README.iso

%build
# don't use configure macro
./configure

%make

%install
rm -fr $RPM_BUILD_ROOT

%makeinstall_std

chmod 644 Copyright README* 

%clean
rm -fr $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc README* Copyright
%{_libdir}/aspell-%{aspell_ver}/*




%changelog
* Mon May 02 2011 Oden Eriksson <oeriksson@mandriva.com> 1.0.0-11mdv2011.0
+ Revision: 662834
- mass rebuild

* Mon Nov 29 2010 Oden Eriksson <oeriksson@mandriva.com> 1.0.0-10mdv2011.0
+ Revision: 603214
- rebuild

* Sun Mar 14 2010 Oden Eriksson <oeriksson@mandriva.com> 1.0.0-9mdv2010.1
+ Revision: 518927
- rebuild

  + Isabel Vallejo <isabel@mandriva.org>
    - update to 1.0-0

* Sun Aug 09 2009 Oden Eriksson <oeriksson@mandriva.com> 0.9.0-7mdv2010.0
+ Revision: 413070
- rebuild

* Fri Mar 06 2009 Antoine Ginies <aginies@mandriva.com> 0.9.0-6mdv2009.1
+ Revision: 350032
- 2009.1 rebuild

* Mon Jun 16 2008 Thierry Vignaud <tv@mandriva.org> 0.9.0-5mdv2009.0
+ Revision: 220383
- rebuild

* Sun Mar 09 2008 Anssi Hannula <anssi@mandriva.org> 0.9.0-4mdv2008.1
+ Revision: 182460
- provide enchant-dictionary

* Fri Jan 11 2008 Thierry Vignaud <tv@mandriva.org> 0.9.0-3mdv2008.1
+ Revision: 148780
- rebuild
- kill re-definition of %%buildroot on Pixel's request
- s/Mandrake/Mandriva/

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot


* Wed Feb 21 2007 Oden Eriksson <oeriksson@mandriva.com> 0.9.0-2mdv2007.0
+ Revision: 123265
- Import aspell-he

* Wed Feb 21 2007 Oden Eriksson <oeriksson@mandriva.com> 0.9.0-2mdv2007.1
- use the mkrel macro
- disable debug packages

* Wed Feb 16 2005 Pablo Saratxaga <pablo@mandrakesoft.com> 0.9.0-1mdk
- updated to new release

* Fri Dec 03 2004 Pablo Saratxaga <pablo@mandrakesoft.com> 0.8.0-1mdk
- first version

