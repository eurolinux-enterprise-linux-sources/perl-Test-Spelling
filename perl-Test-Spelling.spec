Name:           perl-Test-Spelling
Version:        0.19
Release:        1%{?dist}
Summary:        Check for spelling errors in POD files
Group:          Development/Libraries
License:        GPL+ or Artistic
URL:            http://search.cpan.org/dist/Test-Spelling/
Source0:        http://search.cpan.org/CPAN/authors/id/S/SA/SARTAK/Test-Spelling-%{version}.tar.gz
Patch0:         Test-Spelling-0.19-hunspell.patch
BuildArch:      noarch
BuildRequires:  hunspell-en
BuildRequires:  perl(base)
BuildRequires:  perl(Carp)
BuildRequires:  perl(Cwd)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::Path)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(IPC::Run3) >= 0.044
BuildRequires:  perl(Pod::Spell) >= 1.01
BuildRequires:  perl(Test::Builder)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Pod) >= 1.00
BuildRequires:  perl(Test::Tester)
Requires:       perl(:MODULE_COMPAT_%(eval "`perl -V:version`"; echo $version))
Requires:       hunspell
Requires:       perl(Carp)

%description
"Test::Spelling" lets you check the spelling of a POD file, and report
its results in standard "Test::Simple" fashion. This module requires the
hunspell program.

%prep
%setup -q -n Test-Spelling-%{version}

# Promote hunspell over spell/aspell to avoid surprises if aspell is installed
%patch0

# Force the author test to run too
mkdir inc/.author

%build
perl Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
make pure_install DESTDIR=%{buildroot}
find %{buildroot} -type f -name .packlist -exec rm -f {} \;
%{_fixperms} %{buildroot}

%check
make test

%files
%doc Changes README
%{perl_vendorlib}/Test/
%{_mandir}/man3/Test::Spelling.3pm*

%changelog
* Sun May  5 2013 Paul Howarth <paul@city-fan.org> - 0.19-1
- Update to 0.19:
  - For more consistent results, avoid using the user's local aspell dictionary
    (CPAN RT#56483)
- Update hunspell preference patch

* Fri Apr 26 2013 Paul Howarth <paul@city-fan.org> - 0.18-1
- Update to 0.18:
  - Work around Pod::Spell limitations
  - Improve case handling
  - Improve test failure reporting
  - Include more useful info in Test-Spelling's own test suite

* Mon Jan 28 2013 Paul Howarth <paul@city-fan.org> - 0.17-1
- Update to 0.17:
  - Use IPC::Run3 instead of IPC::Open3

* Fri Dec 21 2012 Paul Howarth <paul@city-fan.org> - 0.16-1
- Update to 0.16:
  - Allow use of a custom POD parser rather than Pod::Spell using
    set_pod_parser
- Re-diff patch to avoid shipping .orig file

* Wed Nov 21 2012 Jitka Plesnikova <jplesnik@redhat.com> - 0.15-5
- Update dependencies
- Don't need to remove empty directories from the buildroot
- Drop %%defattr, redundant since rpm 4.4

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.15-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Mon Jun 11 2012 Petr Pisar <ppisar@redhat.com> - 0.15-3
- Perl 5.16 rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.15-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Aug 23 2011 Paul Howarth <paul@city-fan.org> - 0.15-1
- Update to 0.15:
  - Begin adding actual tests (hilariously, adding the suggested t/pod-spell.t
    to this dist to test itself found a typo: "stopwards")
- BR: perl(Test::Tester) and hunspell-en

* Mon Jun 20 2011 Marcela Mašláňová <mmaslano@redhat.com> - 0.14-2
- Perl mass rebuild

* Fri May 27 2011 Paul Howarth <paul@city-fan.org> - 0.14-1
- Update to 0.14:
  - Fix an error when using add_stopwords("constant","strings") (CPAN RT#68471)

* Wed Apr 27 2011 Paul Howarth <paul@city-fan.org> - 0.13-1
- Update to 0.13:
  - Make alternatives checking more robust by reading the spellchecker's STDERR

* Tue Apr 26 2011 Paul Howarth <paul@city-fan.org> - 0.12-1
- Update to 0.12:
  - Best Practical has taken over maintainership of this module
  - Try various spellcheck programs instead of hardcoding the ancient `spell`
    (CPAN RT#56483)
  - Remove temporary files more aggressively (CPAN RT#41586)
  - Fixed by not creating them at all - instead we now use IPC::Open3
  - Remove suggestion to use broken `aspell -l` (CPAN RT#28967)
  - Add set_pod_file_filter for skipping translations, etc. (CPAN RT#63755)
  - Skip tests in all_pod_files_spelling_ok if there is no working spellchecker
  - Provide a has_working_spellchecker so you can skip your own tests if
    there's no working spellchecker
  - Switch to Module::Install
  - Rewrite and modernize a lot of the documentation
  - Decruftify code, such as by using Exporter and lexical filehandles
  - Support .plx files
- This release by SARTAK -> update source URL
- Rewrite hunspell patch to just favour hunspell over aspell
- BR: perl(IPC::Open3)

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.11-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Dec 22 2010 Marcela Maslanova <mmaslano@redhat.com> - 0.11-10
- Rebuild to fix problems with vendorarch/lib (#661697)

* Fri May 07 2010 Marcela Maslanova <mmaslano@redhat.com> - 0.11-9
- Mass rebuild with perl-5.12.0

* Fri Jan 29 2010 Tom "spot" Callaway <tcallawa@redhat.com> - 0.11-8
- actually apply patch. :P

* Wed Jan 20 2010 Tom "spot" Callaway <tcallawa@redhat.com> - 0.11-7
- use hunspell instead of aspell (bz 508643)

* Fri Dec  4 2009 Stepan Kasal <skasal@redhat.com> - 0.11-6
- rebuild against perl 5.10.1

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.11-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.11-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Wed Feb 27 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 0.11-3
- Rebuild for perl 5.10 (again)

* Sun Jan 13 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 0.11-2
- rebuild for new perl

* Tue Dec 19 2006 Jose Pedro Oliveira <jpo at di.uminho.pt> - 0.11-1
- First build.
