function Get-GameMetaDataList {
    [CmdletBinding()]
    Param(

        [Validateset("https://devs.ouya.tv/api/v1", "https://rabid.ouya.tv/api/v1")]
        $BaseUri = "https://devs.ouya.tv/api/v1"

    )

    if (-not $OuyaTVApps) {
        $OuyaTVApps = ((Invoke-WebRequest "$BaseUri/apps").Content | ConvertFrom-Json).apps
    }
    $OuyaTVApps | Foreach-Object {
        $IndividualMetaData = ((Invoke-WebRequest "$BaseUri/apps/$($PSItem.version)").Content | ConvertFrom-Json).app
        if ($IndividualMetaData.Premium) {
            $Premium = ""
        }
        else {
            $Premium = ((Invoke-WebRequest "$BaseUri/apps/$($PSItem.version)/download").Content | ConvertFrom-Json).app | ConvertTo-Json -Compress
        }
        [PSCustomObject]@{
            Title               = $PSItem.Title
            PackageName         = $PSItem.uuid
            LatestVersion       = $IndividualMetaData.versionNumber
            LatestApkMd5sum     = $IndividualMetaData.md5sum
            LatestVersionLength = $IndividualMetaData.apkFileSize
            DownloadUri         = $Premium
            RawAppsJson         = $PSItem #| ConvertTo-Json
            RawAppJson          = $IndividualMetaData #| ConvertTo-Json
        }
    }
}

Get-GameMetaDataList | ConvertTo-Json -Depth 100 | Out-File api.json -Encoding utf8
