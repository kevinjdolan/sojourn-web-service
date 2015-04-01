module.exports = function(grunt) {

    // Project configuration
    grunt.initConfig({
        pkg: grunt.file.readJSON('package.json'),
        appengine: {
            railz: {
                root: '.',
                modules: ['dispatch.yaml', 'app.yaml', 'reporting.yaml'],
                runFlags: {
                    port: 8080,
                    admin_port: 8000,
                    datastore_path: 'datastore',
                    blobstore_path: 'blobstore',
                    automatic_restart: 'yes'
                }
            }
        },
        railz: {
            interim_dir: 'resource-interim',
            output_dir: 'resource/compiled',
            modules: [
                {
                    name: 'client',
                    src: [
                        'lib/railz/resource-src/jquery',
                        'lib/railz/resource-src/base',
                        'resource-src/base', 
                        'resource-src/client'
                    ]
                },
                {
                    name: 'admin',
                    src: [
                        'lib/railz/resource-src/jquery',
                        'lib/railz/resource-src/bootstrap',
                        'lib/railz/resource-src/base',
                        'lib/railz/resource-src/railz-admin',
                        'resource-src/base', 
                        'resource-src/admin'
                    ]
                }
            ]
        },
    });

    grunt.loadNpmTasks('grunt-railz');

};