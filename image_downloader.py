from simple_image_download import simple_image_download as simp
response = simp.simple_image_download
lst=["Maruti car"]
for rep in lst:
 response().download(rep, 50)