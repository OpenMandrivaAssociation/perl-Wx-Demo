
%define realname   Wx-Demo
%define version    0.10
%define release    %mkrel 1

Name:       perl-%{realname}
Version:    %{version}
Release:    %{release}
License:    GPL or Artistic
Group:      Development/Perl
Summary:    The wxPerl demo
Source:     http://www.cpan.org/modules/by-module/Wx/%{realname}-%{version}.tar.gz
Url:        http://search.cpan.org/dist/%{realname}
BuildRoot:  %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires: perl-devel
BuildRequires: perl(Class::Accessor::Fast)
BuildRequires: perl(File::Slurp)
BuildRequires: perl(File::Spec)
BuildRequires: perl(File::chdir)
BuildRequires: perl(IO::Scalar)
BuildRequires: perl(Module::Pluggable)
BuildRequires: perl(UNIVERSAL::require)
BuildRequires: perl(Wx)

BuildArch: noarch

%description
no description found

%prep
%setup -q -n %{realname}-%{version} 

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
#make test

%install
rm -rf %buildroot
%makeinstall_std

%clean
rm -rf %buildroot

%files
%defattr(-,root,root)
%doc Changes
/usr/bin/wxperl_demo.pl
%{_mandir}/man3/*
%perl_vendorlib/*


