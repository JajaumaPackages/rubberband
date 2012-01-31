Name:           rubberband
Version:        1.7.0
Release:        1%{?dist}
Summary:        Audio time-stretching and pitch-shifting library

Group:          System Environment/Libraries
License:        GPLv2+
URL:            http://www.breakfastquay.com/rubberband/
Source0:        http://code.breakfastquay.com/attachments/download/23/rubberband-1.7.0.tar.bz2
Patch0:         %{name}-1.5.0-mk.patch
# incorrect version in configure.ac (harmless) and .pc.in (could be bad
# if a consumer strictly requires 1.5.0 functionality);
# e-mailed to author
Patch1:		%{name}-1.6.0-fix_ver.patch
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
%patch0 -p1 -b .mk
%patch1 -p1 -b .fix_ver
sed -i 's|{exec_prefix}/lib|{exec_prefix}/%{_lib}|' rubberband.pc.in


%build
%configure --disable-static
make %{?_smp_mflags}


%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -name '*.la' -exec rm -f {} ';'
rm -rf $RPM_BUILD_ROOT%{_libdir}/*.a

%clean
rm -rf $RPM_BUILD_ROOT


%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig


%files
%defattr(-,root,root,-)
%doc COPYING README.txt
%{_bindir}/rubberband
%{_libdir}/*.so.*
%{_libdir}/ladspa/ladspa-rubberband.*
%{_datadir}/ladspa/rdf/ladspa-rubberband.rdf
%{_libdir}/vamp/vamp-rubberband.*

%files devel
%defattr(-,root,root,-)
%doc
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/rubberband.pc


%changelog
* Tue Jan 31 2012 Michel Salim <salimma@fedoraproject.org> - 1.7.0-1
- Update to 1.7.0

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Thu Jul 14 2011 Michel Salim <salimma@fedoraproject.org> - 1.6.0-1
- Update to 1.6.0

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sat Jul  3 2010 Michel Salim <salimma@fedoraproject.org> - 1.5.0-2
- Fixed pkg-config version declaration

* Wed Jun  2 2010 Tom "spot" Callaway <tcallawa@redhat.com> - 1.5.0-1
- update to 1.5.0
- disable static libs

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

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

