def write_testfile(filename, collection, identical, product, expected):
#def write_testfile(filename, collection, product, expected):

    file = open(filename, "w")
    file.write("import pytest\n")
    file.write("def test_" + collection + "_" + expected['q_num'] + "_cs():\n")
    file.write("    assert "+"'"+product['gdal_cs']+"'"+" == "+"'"+expected['cs']+"'"+"\n")
    file.write("def test_" + collection + "_" + expected['q_num'] +"_projection():\n")
    file.write("    assert "+"'"+product['gdal_proj_cs']+"'"+" == "+"'"+expected['proj_cs']+"'"+"\n")
    file.write("def test_" + collection + "_" + expected['q_num'] +"_proj_epsg():\n")
    file.write("    assert "+"'"+product['gdal_proj_epsg']+"'"+" == "+"'"+expected['proj_epsg']+"'"+"\n")
    file.write("def test_" + collection + "_" + expected['q_num'] +"_gcs():\n")
    file.write("    assert "+"'"+product['gdal_gcs']+"'"+" == "+"'"+expected['gcs']+"'"+"\n")
    file.write("def test_" + collection + "_" + expected['q_num'] +"_gcs_epsg():\n")
    file.write("    assert "+"'"+product['gdal_gcs_epsg']+"'"+" == "+"'"+expected['gcs_epsg']+"'"+"\n")
    file.write("def test_" + collection + "_" + expected['q_num'] +"_authority():\n")
    file.write("    assert "+"'"+product['gdal_authority']+"'"+" == "+"'"+expected['authority']+"'"+"\n")
    file.write("def test_" + collection + "_" + expected['q_num'] +"_subset():\n")
    file.write("    assert "+str(product['gdal_spatial_extent'])+" == "+str(expected['subset'])+"\n")
    file.write("def test_" + collection + "_" + expected['q_num'] +"_bands():\n")
    file.write("    assert "+str(product['gdal_n_bands'])+" == "+str(expected['bands'])+"\n")
    file.write("def test_" + collection + "_" + expected['q_num'] +"_variables():\n")
    file.write("    assert "+str(product['gdal_variables'])+" == "+str(expected['variables'])+"\n")
    file.write("def test_" + collection + "_" + expected['q_num'] +"_xy_size():\n")
    file.write("    assert "+str(product['gdal_xy_size'])+" == "+str(expected['xy_size'])+"\n")
    file.write("def test_" + collection + "_" + expected['q_num'] +"_identical_to_reference_image():\n")
    file.write("    assert "+"'"+str(identical)+"'"+" == "+"'"+"True"+"'"+"\n")
    file.close()

    return
