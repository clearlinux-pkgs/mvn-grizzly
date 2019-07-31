#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : mvn-grizzly
Version  : 2.2.21
Release  : 1
URL      : https://github.com/javaee/grizzly/archive/2_2_21.tar.gz
Source0  : https://github.com/javaee/grizzly/archive/2_2_21.tar.gz
Source1  : https://repo1.maven.org/maven2/org/glassfish/grizzly/grizzly-framework/2.2.21/grizzly-framework-2.2.21.jar
Source2  : https://repo1.maven.org/maven2/org/glassfish/grizzly/grizzly-framework/2.2.21/grizzly-framework-2.2.21.pom
Source3  : https://repo1.maven.org/maven2/org/glassfish/grizzly/grizzly-http-server/2.2.21/grizzly-http-server-2.2.21.jar
Source4  : https://repo1.maven.org/maven2/org/glassfish/grizzly/grizzly-http-server/2.2.21/grizzly-http-server-2.2.21.pom
Source5  : https://repo1.maven.org/maven2/org/glassfish/grizzly/grizzly-http-servlet/2.2.21/grizzly-http-servlet-2.2.21.jar
Source6  : https://repo1.maven.org/maven2/org/glassfish/grizzly/grizzly-http-servlet/2.2.21/grizzly-http-servlet-2.2.21.pom
Source7  : https://repo1.maven.org/maven2/org/glassfish/grizzly/grizzly-http/2.2.21/grizzly-http-2.2.21.jar
Source8  : https://repo1.maven.org/maven2/org/glassfish/grizzly/grizzly-http/2.2.21/grizzly-http-2.2.21.pom
Source9  : https://repo1.maven.org/maven2/org/glassfish/grizzly/grizzly-project/2.2.21/grizzly-project-2.2.21.pom
Source10  : https://repo1.maven.org/maven2/org/glassfish/grizzly/grizzly-rcm/2.2.21/grizzly-rcm-2.2.21.jar
Source11  : https://repo1.maven.org/maven2/org/glassfish/grizzly/grizzly-rcm/2.2.21/grizzly-rcm-2.2.21.pom
Summary  : No detailed summary available
Group    : Development/Tools
License  : Apache-2.0 CDDL-1.0 GPL-2.0
Requires: mvn-grizzly-data = %{version}-%{release}
BuildRequires : apache-ant
BuildRequires : buildreq-mvn

%description
The sample demonstrates how easy Grizzly HttpServer could be configured to process both HTTP and AJP requests.
All we need to do is register AjpAddOn on corresponding HTTP NetworkListener (see the code).

%package data
Summary: data components for the mvn-grizzly package.
Group: Data

%description data
data components for the mvn-grizzly package.


%prep

%build

%install
mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/glassfish/grizzly/grizzly-framework/2.2.21
cp %{SOURCE1} %{buildroot}/usr/share/java/.m2/repository/org/glassfish/grizzly/grizzly-framework/2.2.21/grizzly-framework-2.2.21.jar

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/glassfish/grizzly/grizzly-framework/2.2.21
cp %{SOURCE2} %{buildroot}/usr/share/java/.m2/repository/org/glassfish/grizzly/grizzly-framework/2.2.21/grizzly-framework-2.2.21.pom

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/glassfish/grizzly/grizzly-http-server/2.2.21
cp %{SOURCE3} %{buildroot}/usr/share/java/.m2/repository/org/glassfish/grizzly/grizzly-http-server/2.2.21/grizzly-http-server-2.2.21.jar

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/glassfish/grizzly/grizzly-http-server/2.2.21
cp %{SOURCE4} %{buildroot}/usr/share/java/.m2/repository/org/glassfish/grizzly/grizzly-http-server/2.2.21/grizzly-http-server-2.2.21.pom

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/glassfish/grizzly/grizzly-http-servlet/2.2.21
cp %{SOURCE5} %{buildroot}/usr/share/java/.m2/repository/org/glassfish/grizzly/grizzly-http-servlet/2.2.21/grizzly-http-servlet-2.2.21.jar

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/glassfish/grizzly/grizzly-http-servlet/2.2.21
cp %{SOURCE6} %{buildroot}/usr/share/java/.m2/repository/org/glassfish/grizzly/grizzly-http-servlet/2.2.21/grizzly-http-servlet-2.2.21.pom

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/glassfish/grizzly/grizzly-http/2.2.21
cp %{SOURCE7} %{buildroot}/usr/share/java/.m2/repository/org/glassfish/grizzly/grizzly-http/2.2.21/grizzly-http-2.2.21.jar

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/glassfish/grizzly/grizzly-http/2.2.21
cp %{SOURCE8} %{buildroot}/usr/share/java/.m2/repository/org/glassfish/grizzly/grizzly-http/2.2.21/grizzly-http-2.2.21.pom

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/glassfish/grizzly/grizzly-project/2.2.21
cp %{SOURCE9} %{buildroot}/usr/share/java/.m2/repository/org/glassfish/grizzly/grizzly-project/2.2.21/grizzly-project-2.2.21.pom

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/glassfish/grizzly/grizzly-rcm/2.2.21
cp %{SOURCE10} %{buildroot}/usr/share/java/.m2/repository/org/glassfish/grizzly/grizzly-rcm/2.2.21/grizzly-rcm-2.2.21.jar

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/glassfish/grizzly/grizzly-rcm/2.2.21
cp %{SOURCE11} %{buildroot}/usr/share/java/.m2/repository/org/glassfish/grizzly/grizzly-rcm/2.2.21/grizzly-rcm-2.2.21.pom


%files
%defattr(-,root,root,-)

%files data
%defattr(-,root,root,-)
/usr/share/java/.m2/repository/org/glassfish/grizzly/grizzly-framework/2.2.21/grizzly-framework-2.2.21.jar
/usr/share/java/.m2/repository/org/glassfish/grizzly/grizzly-framework/2.2.21/grizzly-framework-2.2.21.pom
/usr/share/java/.m2/repository/org/glassfish/grizzly/grizzly-http-server/2.2.21/grizzly-http-server-2.2.21.jar
/usr/share/java/.m2/repository/org/glassfish/grizzly/grizzly-http-server/2.2.21/grizzly-http-server-2.2.21.pom
/usr/share/java/.m2/repository/org/glassfish/grizzly/grizzly-http-servlet/2.2.21/grizzly-http-servlet-2.2.21.jar
/usr/share/java/.m2/repository/org/glassfish/grizzly/grizzly-http-servlet/2.2.21/grizzly-http-servlet-2.2.21.pom
/usr/share/java/.m2/repository/org/glassfish/grizzly/grizzly-http/2.2.21/grizzly-http-2.2.21.jar
/usr/share/java/.m2/repository/org/glassfish/grizzly/grizzly-http/2.2.21/grizzly-http-2.2.21.pom
/usr/share/java/.m2/repository/org/glassfish/grizzly/grizzly-project/2.2.21/grizzly-project-2.2.21.pom
/usr/share/java/.m2/repository/org/glassfish/grizzly/grizzly-rcm/2.2.21/grizzly-rcm-2.2.21.jar
/usr/share/java/.m2/repository/org/glassfish/grizzly/grizzly-rcm/2.2.21/grizzly-rcm-2.2.21.pom
