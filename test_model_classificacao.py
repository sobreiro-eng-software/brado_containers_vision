# This is an automatically generated code sample.
# To make this code sample work in your Oracle Cloud tenancy,
# please replace the values for any parameters whose current values do not fit
# your use case (such as resource IDs, strings containing ‘EXAMPLE’ or ‘unique_id’, and
# boolean, number, and enum parameters with values not fitting your use case).

import oci
import base64

# Create a default config using DEFAULT profile in default location
# Refer to
# https://docs.cloud.oracle.com/en-us/iaas/Content/API/Concepts/sdkconfig.htm#SDK_and_CLI_Configuration_File
# for more info
config = oci.config.from_file("/home/sobreiro/.oci/config", "functions-developer-profile")  # Provide the config file path

# Initialize service client with default config file
ai_vision_client = oci.ai_vision.AIServiceVisionClient(config)

# Preparing data
ocr_image = "brado3.png"  # Provide the image location
with open(ocr_image, "rb") as image_file:
    encoded_string = base64.b64encode(image_file.read())


# Send the request to service, some parameters are not required, see API
# doc for more info
analyze_image_response = ai_vision_client.analyze_image(
    analyze_image_details=oci.ai_vision.models.AnalyzeImageDetails(
        features=[
            oci.ai_vision.models.ImageClassificationFeature(
                feature_type="IMAGE_CLASSIFICATION",
                max_results=50,
                model_id="ocid1.aivisionmodel.oc1.sa-saopaulo-1.amaaaaaakm2rzfqajikvu5mi4imgz6gjhk2u4qo2j54uqm5etiwo4s7ooylq",
            )
        ],
        image=oci.ai_vision.models.InlineImageDetails(
            source="INLINE", data=encoded_string.decode("utf-8")
        ),
        compartment_id="ocid1.compartment.oc1..aaaaaaaav3se6eugwjeujk2exs6sf4uitigsl2iwaetkhrpdz7qocyxhonsq",
    ),
)

# Get the data from response
print(analyze_image_response.data)
