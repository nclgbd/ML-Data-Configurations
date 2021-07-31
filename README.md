# ML Data Configurations
Contains a template for how to expect data to be laid out.

# Configuration Setup:
```javascript
{
    // json object containing the different configurations
    "avail_configs": { 
        // configuration name
        "configuration1": {
            "classes": [ 
            // the names of the available classes
                "class1",
                "class2"
            ],
            "format": {
                // contains the number of classes
                "num_of_classes": 2,
                "sort_by": "tag1"
            }
        },

        .
        .
        .
    },
    // the name of the available tags
    "avail_tags": [
        "configuration1",
                .
                .
                .
        "configurationN"
    ]
    
}
```
