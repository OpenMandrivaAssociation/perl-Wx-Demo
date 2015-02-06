%define upstream_name    Wx-Demo
%define upstream_version 0.22
%define __noautoreq 'perl\\(Wx::PlHeaderColumn\\)|perl\\(Wx::PlHeaderCtrl\\)|perl\\(Wx::Demo.*'

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	4

License:	GPL+ or Artistic
Group:		Development/Perl
Summary:	The wxPerl demo

Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/Wx/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(Class::Accessor::Fast)
BuildRequires:	perl(File::Slurp)
BuildRequires:	perl(File::Spec)
BuildRequires:	perl(File::chdir)
BuildRequires:	perl(IO::Scalar)
BuildRequires:	perl(Module::Pluggable)
BuildRequires:	perl(UNIVERSAL::require)
BuildRequires:	perl(Wx)
BuildArch:	noarch

%description
wxPerl demo, with lots of snippets using various wxwidgets features.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
#make test

%install
%makeinstall_std

%files
%doc Changes
%{_bindir}/wxperl_demo.pl
%{_mandir}/man3/*
%{perl_vendorlib}/*



