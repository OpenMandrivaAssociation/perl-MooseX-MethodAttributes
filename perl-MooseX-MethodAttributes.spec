%define upstream_name    MooseX-MethodAttributes%define upstream_version 0.29

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    3

Summary:    No summary found
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/MooseX/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires: perl(Moose)
BuildRequires: perl(Test::Requires)
BuildRequires: perl(Test::Fatal)
BuildRequires: perl(MooseX::Types)
BuildRequires: perl(Test::CheckDeps)
BuildRequires: perl(Test::Exception)
BuildRequires: perl(Test::More)
BuildRequires: perl(namespace::autoclean)
BuildRequires: perl(namespace::clean)
BuildRequires: perl-devel

BuildArch: noarch

%description
This module allows code attributes of methods to be introspected using
Moose meta method objects.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
%makeinstall_std

%files
%doc Changes LICENSE README
%{_mandir}/man3/*
%perl_vendorlib/*


%changelog
* Wed Jun 22 2011 Guillaume Rousse <guillomovitch@mandriva.org> 0.250.0-1mdv2011.0
+ Revision: 686643
- update to new version 0.25

* Mon Apr 18 2011 Funda Wang <fwang@mandriva.org> 0.240.0-2
+ Revision: 655081
- rebuild for updated spec-helper

* Tue Jul 27 2010 Jérôme Quelin <jquelin@mandriva.org> 0.240.0-1mdv2011.0
+ Revision: 561097
- adding missing buildrequires:
- update to 0.24

* Tue Jul 13 2010 Jérôme Quelin <jquelin@mandriva.org> 0.230.0-1mdv2011.0
+ Revision: 552419
- update to 0.23

* Wed Feb 10 2010 Jérôme Quelin <jquelin@mandriva.org> 0.200.0-1mdv2010.1
+ Revision: 503784
- update to 0.20

* Sun Jan 10 2010 Jérôme Quelin <jquelin@mandriva.org> 0.190.0-1mdv2010.1
+ Revision: 488603
- update to 0.19

* Sat Sep 26 2009 Jérôme Quelin <jquelin@mandriva.org> 0.180.0-1mdv2010.0
+ Revision: 449365
- update to 0.18

* Thu Sep 24 2009 Jérôme Quelin <jquelin@mandriva.org> 0.170.0-1mdv2010.0
+ Revision: 448124
- update to 0.17

* Tue Sep 15 2009 Jérôme Quelin <jquelin@mandriva.org> 0.160.0-1mdv2010.0
+ Revision: 442943
- update to 0.16

* Mon Jul 27 2009 Jérôme Quelin <jquelin@mandriva.org> 0.150.0-1mdv2010.0
+ Revision: 400651
- update to 0.15

* Fri Jun 12 2009 Jérôme Quelin <jquelin@mandriva.org> 0.140.0-1mdv2010.0
+ Revision: 385440
- import perl-MooseX-MethodAttributes


* Fri Jun 12 2009 cpan2dist 0.14-1mdv
- initial mdv release, generated with cpan2dist


