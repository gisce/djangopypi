from django.conf import settings

# This is disabled on pypi.python.org, can be useful if you make mistakes
if not hasattr(settings,'DJANGOPYPI_ALLOW_VERSION_OVERWRITE'):
    settings.DJANGOPYPI_ALLOW_VERSION_OVERWRITE = False

""" The upload_to argument for the file field in releases. This can either be 
a string for a path relative to your media folder or a callable. For more 
information, see http://docs.djangoproject.com/ """
if not hasattr(settings,'DJANGOPYPI_RELEASE_UPLOAD_TO'):
    settings.DJANGOPYPI_RELEASE_UPLOAD_TO = 'dists'

if not hasattr(settings,'DJANGOPYPI_OS_NAMES'):
    settings.DJANGOPYPI_OS_NAMES = (
        ("aix", "AIX"),
        ("beos", "BeOS"),
        ("debian", "Debian Linux"),
        ("dos", "DOS"),
        ("freebsd", "FreeBSD"),
        ("hpux", "HP/UX"),
        ("mac", "Mac System x."),
        ("macos", "MacOS X"),
        ("mandrake", "Mandrake Linux"),
        ("netbsd", "NetBSD"),
        ("openbsd", "OpenBSD"),
        ("qnx", "QNX"),
        ("redhat", "RedHat Linux"),
        ("solaris", "SUN Solaris"),
        ("suse", "SuSE Linux"),
        ("yellowdog", "Yellow Dog Linux"),
    )

if not hasattr(settings,'DJANGOPYPI_ARCHITECTURES'):
    settings.DJANGOPYPI_ARCHITECTURES = (
        ("alpha", "Alpha"),
        ("hppa", "HPPA"),
        ("ix86", "Intel"),
        ("powerpc", "PowerPC"),
        ("sparc", "Sparc"),
        ("ultrasparc", "UltraSparc"),
    )

if not hasattr(settings,'DJANGOPYPI_DIST_FILE_TYPES'):
    settings.DJANGOPYPI_DIST_FILE_TYPES = (
        ('sdist','Source'),
        ('bdist_dumb','"dumb" binary'),
        ('bdist_rpm','RPM'),
        ('bdist_wininst','MS Windows installer'),
        ('bdist_egg','Python Egg'),
        ('bdist_dmg','OS X Disk Image'),
    )

if not hasattr(settings,'DJANGOPYPI_PYTHON_VERSIONS'):
    settings.DJANGOPYPI_PYTHON_VERSIONS = (
        ('any','Any i.e. pure python'),
        ('2.1','2.1'),
        ('2.2','2.2'),
        ('2.3','2.3'),
        ('2.4','2.4'),
        ('2.5','2.5'),
        ('2.6','2.6'),
        ('2.7','2.7'),
        ('3.0','3.0'),
        ('3.1','3.1'),
        ('3.2','3.2'),
    )

if not hasattr(settings, 'DJANGOPYPI_FALLBACK_VIEW'):
    from djangopypi.views import releases 
    settings.DJANGOPYPI_FALLBACK_VIEW = releases.index

if not hasattr(settings,'DJANGOPYPI_ACTION_VIEWS'):
    from djangopypi.views.distutils import register_or_upload
    
    settings.DJANGOPYPI_ACTION_VIEWS = {
        "file_upload": register_or_upload, #``sdist`` command
        "submit": register_or_upload, #``register`` command
    }

if not hasattr(settings, 'DJANGOPYPI_METADATA_FIELDS'):
    settings.DJANGOPYPI_METADATA_FIELDS = {
        '1.0': ('platform','summary','description','keywords','home_page',
                'author','author_email', 'license', 'classifier'),
        '1.1': ('platform','supported_platform','summary','description',
                'keywords','home_page','download_url','author','author_email',
                'license','classifier','requires','provides','obsoletes',),
        '1.2': ('platform','supported_platform','summary','description',
                'keywords','home_page','download_url','author','author_email',
                'maintainer','maintainer_email','license','classifier',
                'requires_dist','provides_dist','obsoletes_dist',
                'requires_python','requires_external','project_url')}
    