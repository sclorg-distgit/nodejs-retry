%{?scl:%scl_package nodejs-retry}
%{!?scl:%global pkg_name %{name}}
%{?nodejs_find_provides_and_requires}

Name:           %{?scl_prefix}nodejs-retry
Version:        0.10.1
Release:        1%{?dist}
Summary:        Retry strategies for failed operations
BuildArch:      noarch
ExclusiveArch:  %{nodejs_arches} noarch
License:        MIT
URL:            https://github.com/felixge/node-retry
Source0:        http://registry.npmjs.org/retry/-/retry-%{version}.tgz

BuildRequires:  %{?scl_prefix}nodejs-devel

%description
Abstraction for exponential and custom retry strategies for failed operations.

%prep
%setup -q -n package

%build
#nothing to do

%install
mkdir -p %{buildroot}%{nodejs_sitelib}/retry
cp -pr package.json index.js lib %{buildroot}%{nodejs_sitelib}/retry

%nodejs_symlink_deps


%files
%{nodejs_sitelib}/retry
%doc License README.md equation.gif example

%changelog
* Thu Jan 05 2017 Zuzana Svetlikova <zsvetlik@redhat.com> - 0.10.1-1
- Updated with script

* Thu Sep 15 2016 Zuzana Svetlikova <zsvetlik@redhat.com> - 0.9.0-1
- Updated with script

* Tue Feb 16 2016 Tomas Hrcka <thrcka@redhat.com> - 0.9.0-1
- New upstream release 0.9.0

* Sun Feb 14 2016 Zuzana Svetlikova <zsvetlik@redhat.com> - 0.6.0-7
- rebuilt

* Thu Feb 27 2014 Tomas Hrcka <thrcka@redhat.com> - 0.6.0-6
- Rebuilt rhbz#(1070612)

* Thu Oct 17 2013 Tomas Hrcka <thrcka@redhat.com> - 0.6.0-5
- replace provides and requires with macro

* Thu Apr 11 2013 Stanislav Ochotnicky <sochotnicky@redhat.com> - 0.6.0-4
- Add support for software collections

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Tue Jan 08 2013 T.C. Hollingsworth <tchollingsworth@gmail.com> - 0.6.0-2
- add missing build section
- fix License tag

* Mon Dec 31 2012 T.C. Hollingsworth <tchollingsworth@gmail.com> - 0.6.0-1
- initial package generated by npm2rpm
