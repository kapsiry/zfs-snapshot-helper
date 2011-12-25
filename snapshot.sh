function zfs-snapshots () {
    if [[ $PWD =~ "/.zfs" ]]; then
        echo "Not supported under .zfs directory"
        return
    fi
    local oIFS
    declare -A snapshots
    oIFS=$IFS
    IFS=$'\t' # the display name and path are \t separated, \0 terminated
    snapshot_list=()
    while read -d $'\0' display path; do
        snapshots[$display]=$path
        snapshot_list=(${snapshot_list[@]-} $display)
    done < <(/usr/local/snapshot-helper/zfs-findsnapshot.py)
    if [[ -z ${snapshot_list} ]]; then
        echo "No snapshots found here"
        return
    fi
    select snapshot in ${snapshot_list[@]}; do
        pushd ${snapshots[$snapshot]}
        break;
    done
    IFS=$oIFS
}
