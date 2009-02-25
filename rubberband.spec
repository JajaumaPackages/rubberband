Name:           rubberband
Version:        1.2
Release:        4%{?dist}
Summary:        Audio time-stretching and pitch-shifting library

Group:          System Environment/Libraries
License:        GPLv2+
URL:            http://www.breakfastquay.com/rubberband/
Source0:        http://www.breakfastquay.com/rubberband/files/rubberband-%{version}.tar.bz2
Patch0:         rubberband-1.2-gcc43.patch
Patch1:         rubberband-1.2-gcc44.patch
Patch2:         rubberband-1.2-mk.patch
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires:  fftw-devel libsamplerate-devel libsndfile-devel
BuildRequires:  ladspa-devel vamp-plugin-sdk-devel
Requires:       ladspa

%description
Rubber Band is a library and utility program that permits you to change the
tempo and pitch of an audio recording independently of one another. 


%package        devel
Summary:        Development files for %{name}
Group:          Development/Libraries
Requires:       %{name} = %{version}-%{release}
Requires:       pkgconfig

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%prep
%setup -q
%patch0 -p1 -b .gcc43
%patch1 -p1 -b .gcc44
%patch2 -p1 -b .mk


%build
%configure --disable-static
make %{?_smp_mflags}


%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -name '*.la' -exec rm -f {} ';'


%clean
rm -rf $RPM_BUILD_ROOT


%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig


%files
%defattr(-,root,root,-)
%doc COPYING README
%{_bindir}/rubberband
%{_libdir}/*.so.*
%{_libdir}/ladspa/ladspa-rubberband.*
%{_datadir}/ladspa/rdf/ladspa-rubberband.rdf
%{_libdir}/vamp/vamp-rubberband.*

%files devel
%defattr(-,root,root,-)
%doc
%{_includedir}/*
%{_libdir}/*.a
%{_libdir}/*.so
%{_libdir}/pkgconfig/rubberband.pc


%changelog
* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sun Feb  8 2009 Michel Salim <salimma@fedoraproject.org> - 1.2-3
- Fix compilation problem with GCC 4.4

* Sun Dec 14 2008 Michel Salim <salimma@fedoraproject.org> - 1.2-2
- Rebuild for vamp-plugins-sdk-2.0

* Thu Jul 17 2008 Michel Alexandre Salim <salimma@fedoraproject.org> - 1.2-1
- Update to 1.2

* Sun Mar 30 2008 Michel Salim <michel.sylvan@gmail.com> - 1.0.1-1
- Initial package

