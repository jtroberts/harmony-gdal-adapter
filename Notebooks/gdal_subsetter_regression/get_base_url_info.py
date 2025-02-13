def get_base_url_info(env,collection):

    base_url_info = {'base_url':'',
                     'collection_id':'',
                     'granule_env_flag':''
                    }
    if env == 'prod':
        base_url_info['base_url'] = 'https://harmony.earthdata.nasa.gov/'
        base_url_info['granule_env_flag'] = 'prod_gid'
        if collection == 's1_insar':
            base_url_info['collection_id'] = 'C1595422627-ASF'
        elif collection == 'uavsar':
            base_url_info['collection_id'] = 'C1214354031-ASF'
        elif collection == 'avnir':
            base_url_info['collection_id'] = 'C1808440897-ASF'
        elif collection == 'alos_rt1':
            base_url_info['collection_id'] = 'C1206487504-ASF'
        elif collection == 'alos_rt2':
            base_url_info['collection_id'] = 'C1206487217-ASF'
        elif collection == 'alos_l22':
            base_url_info['collection_id'] = 'C2011599335-ASF'
    elif env == 'uat':
        base_url_info['base_url'] = 'https://harmony.uat.earthdata.nasa.gov/'
        base_url_info['granule_env_flag'] = 'uat_gid'
        if collection == 's1_insar':
            base_url_info['collection_id'] = 'C1225776654-ASF'
        elif collection == 'uavsar':
            base_url_info['collection_id'] = 'C1207038647-ASF'
        elif collection == 'avnir':
            base_url_info['collection_id'] = 'C1233629671-ASF'
        elif collection == 'alos_rt1':
            base_url_info['collection_id'] = 'C1207181535-ASF'
        elif collection == 'alos_rt2':
            base_url_info['collection_id'] = 'C1208013295-ASF'
        elif collection == 'alos_l22':
            base_url_info['collection_id'] = 'C1239927797-ASF'
    elif env == 'sit':
        base_url_info['base_url'] = 'https://harmony.sit.earthdata.nasa.gov/'
        base_url_info['granule_env_flag'] = 'sit_gid'
        if collection == 's1_insar':
            base_url_info['collection_id'] = 'C1225776654-ASF'
        elif collection == 'uavsar':
            base_url_info['collection_id'] = 'C1207038647-ASF'
        elif collection == 'avnir':
            base_url_info['collection_id'] = 'C1233629671-ASF'
        elif collection == 'alos_rt1':
            base_url_info['collection_id'] = 'C1207181535-ASF'
        elif collection == 'alos_rt2':
            base_url_info['collection_id'] = 'C1208013295-ASF'
        elif collection == 'alos_l22':
            base_url_info['collection_id'] = 'C1239927797-ASF'

    return(base_url_info)
